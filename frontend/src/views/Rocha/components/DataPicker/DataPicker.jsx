import * as React from "react"

import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"

import { Button } from "@/components/ui/button"
import { Calendar } from "@/components/ui/calendar"
import { Calendar as CalendarIcon } from "lucide-react"
import { cn } from "@/lib/utils"
import { format } from "date-fns"
import { ptBR } from 'date-fns/locale';

const DataPicker = () => {
  const [date, setDate] = React.useState(new Date())

  return (
    <Popover>
      <PopoverTrigger asChild>
        <Button
          variant={""}
          className={cn(
            "w-[200px] justify-start text-left font-normal bg-white input-field h-7 border border-gray-200 rounded text-sm px-2",
            !date && "text-muted-foreground"
          )}
        >
          <CalendarIcon className="mr-2 h-4 w-4" />
          {date ? format(date, "PPP", { locale: ptBR }) : <span>Pick a date</span>}
        </Button>
      </PopoverTrigger>
      <PopoverContent className="w-auto p-0">
        <Calendar
          mode="single"
          selected={date}
          onSelect={setDate}
          initialFocus
        />
      </PopoverContent>
    </Popover>
  )
}

export default DataPicker