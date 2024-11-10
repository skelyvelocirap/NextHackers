import { Badge } from "./ui/badge";

export default function SkillTag({ children, varient, onClick, isSelected }) {
  return (
    <Badge
      onClick={onClick}
      className={`cursor-pointer bg-background border border-border text-foreground active:text-foreground ${
        varient === "small" ? "text-xs" : "text-sm"
      } ${
        isSelected ? "bg-primary text-primary-foreground" : "hover:bg-muted/50"
      }
       ${
         varient !== "small"
           ? "hover:scale-105 transition-all duration-200 ease-out"
           : "hover:bg-background"
       } `}
    >
      {children}
    </Badge>
  );
}
