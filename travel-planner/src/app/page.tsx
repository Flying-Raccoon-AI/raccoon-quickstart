"use client";

import { useState, useEffect, useRef } from "react";
import { ToolInvocation } from "ai";
import { useChat, Message } from "ai/react";
import { Send, Loader2 } from "lucide-react";
import { marked } from "marked";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";
import FlightCard, { Flight } from "@/components/FlightCard";
import HotelCard, { Hotel } from "@/components/HotelCard";

export default function Chat() {
  const inputRef = useRef<HTMLInputElement>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const [isTyping, setIsTyping] = useState(false);

  const { messages, input, handleInputChange, handleSubmit, isLoading } =
    useChat({
      onFinish: (_) => {
        if (inputRef.current) {
          inputRef.current.focus();
        }
      },
    });

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!input.trim()) return;

    setIsTyping(true);
    handleSubmit(e);
    setIsTyping(false);
  };

  const renderRawMessage = (content: string) => {
    const htmlContent = marked(content);
    return (
      <div
        className="prose prose-sm dark:prose-invert max-w-none p-0 m-0"
        dangerouslySetInnerHTML={{ __html: htmlContent }}
      />
    );
  };

  const renderLoadingState = (toolCallId: string, text: string) => (
    <div
      key={toolCallId}
      className="flex items-center gap-2 text-muted-foreground"
    >
      <Loader2 className="w-4 h-4 animate-spin" />
      <span>{text}</span>
    </div>
  );

  const renderFlightResults = (toolInvocation: ToolInvocation) => {
    if (toolInvocation.state === "call") {
      return renderLoadingState(
        toolInvocation.toolCallId,
        "Searching for flights..."
      );
    } else if (toolInvocation.state === "result") {
      const flightData = toolInvocation.result?.data;
      const hasFlights = Array.isArray(flightData) && flightData.length > 0;

      return (
        <div key={toolInvocation.toolCallId} className="space-y-3">
          {hasFlights
            ? flightData.map((flight: Flight, i: number) => (
                <FlightCard key={`${flight.name}-${i}`} flight={flight} />
              ))
            : "No flights found."}
        </div>
      );
    }
  };

  const renderHotelResults = (toolInvocation: ToolInvocation) => {
    if (toolInvocation.state === "call") {
      return renderLoadingState(
        toolInvocation.toolCallId,
        "Searching for hotels..."
      );
    } else if (toolInvocation.state === "result") {
      const hotelData = toolInvocation.result?.data;
      const hasHotels = Array.isArray(hotelData) && hotelData.length > 0;

      return (
        <div key={toolInvocation.toolCallId} className="space-y-3">
          {hasHotels
            ? hotelData.map((hotel: Hotel, i: number) => (
                <HotelCard key={`${hotel.name}-${i}`} hotel={hotel} />
              ))
            : "No hotels found."}
        </div>
      );
    }
  };

  const renderToolResults = (toolInvocations: ToolInvocation[]) => {
    return toolInvocations.map((t) => {
      if (t.toolName === "flights") return renderFlightResults(t);
      if (t.toolName === "hotels") return renderHotelResults(t);
      return null;
    });
  };

  const parseMessage = (m: Message) => {
    return (
      <div className="space-y-4">
        {m.content && renderRawMessage(m.content)}
        {m.toolInvocations &&
          m.toolInvocations?.length > 0 &&
          renderToolResults(m.toolInvocations)}
      </div>
    );
  };

  return (
    <div className="flex flex-col h-screen max-w-3xl mx-auto bg-gradient-to-b from-background to-secondary/10">
      <header className="sticky top-0 z-10 backdrop-blur-sm bg-background/80 border-b p-4">
        <h1 className="text-2xl font-bold text-center bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
          AI Itinerary Planner
        </h1>
      </header>

      <ScrollArea className="flex-grow p-4 space-y-6 scroll-area">
        {messages.map((m) => (
          <div
            key={m.id}
            className={`flex ${
              m.role === "user" ? "justify-end" : "justify-start"
            } animate-in fade-in slide-in-from-bottom-2`}
          >
            <div
              className={`max-w-[85%] p-3 my-2 rounded-lg shadow-md ${
                m.role === "user"
                  ? "bg-primary text-primary-foreground ml-auto"
                  : "bg-card hover:bg-card/90 transition-colors"
              }`}
            >
              {parseMessage(m)}
            </div>
          </div>
        ))}
        {isTyping && (
          <div className="flex justify-start animate-in fade-in">
            <div className="max-w-[85%] p-4 rounded-2xl bg-card shadow-md">
              <Loader2 className="w-5 h-5 animate-spin" />
            </div>
          </div>
        )}
        <div ref={messagesEndRef} className="h-6" />
      </ScrollArea>

      <footer className="sticky bottom-0 z-10 backdrop-blur-sm bg-background/80 border-t p-4">
        <form onSubmit={onSubmit} className="flex gap-2 max-w-3xl mx-auto">
          <Input
            value={input}
            ref={inputRef}
            onChange={handleInputChange}
            placeholder="Ask about flights or hotels..."
            className="flex-grow rounded-full shadow-sm"
            disabled={isLoading || isTyping}
            autoFocus
          />
          <Button
            type="submit"
            disabled={isLoading || isTyping}
            className="rounded-full px-4 hover:scale-105 transition-transform"
          >
            {isLoading || isTyping ? (
              <Loader2 className="w-4 h-4 animate-spin" />
            ) : (
              <Send className="w-4 h-4" />
            )}
          </Button>
        </form>
      </footer>
    </div>
  );
}
