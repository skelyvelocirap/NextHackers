import Link from "next/link";
import Logo from "./logo";
import { Button } from "./ui/button";

export default function Navbar() {
  return (
    <header className="absolute top-0 inset-y-0 w-full py-6 px-10">
      <div className=" flex justify-between items-center w-full">
        <div className=" flex justify-start items-center gap-10">
          <Logo />
        </div>
        <div className="flex justify-center items-center gap-2">
          <Button variant="ghost">Login</Button>
          <Button>Join</Button>
        </div>
      </div>
    </header>
  );
}
