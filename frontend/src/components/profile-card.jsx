import Link from "next/link";
import { Badge } from "./ui/badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "./ui/card";
import SkillTag from "./skill-tag";
import Image from "next/image";

export default function ProfileCard({ name, title, image, skills }) {
  return (
    <Link href="/" className="">
      <Card className="hover:scale-[103%] transition-all duration-200 ease-out hover:shadow-lg h-full flex flex-col justify-between items-center">
        <CardHeader className="flex flex-col gap-1 justify-start items-center text-center">
          <div className="relative size-20 rounded-full bg-slate-400 shadow-inner overflow-hidden">
            <Image
              className="absolute object-cover"
              fill
              src={image}
              alt={name}
            />
          </div>
          <div>
            <CardTitle className="text-lg font-semibold">{name}</CardTitle>
            <CardDescription>{title}</CardDescription>
          </div>
        </CardHeader>
        <CardContent>
          {skills && (
            <div className="flex flex-wrap gap-2">
              {skills.map((skill) => (
                <SkillTag key={skill.skillId} varient="small">
                  {skill.skillName}
                </SkillTag>
              ))}
            </div>
          )}
        </CardContent>
      </Card>
    </Link>
  );
}
