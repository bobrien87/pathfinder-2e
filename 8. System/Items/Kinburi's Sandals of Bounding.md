---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 700}"
usage: "wornshoes"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These elevated wooden sandals once belonged to a haughty kitsune named Kinburi. It was well known that her swiftness and grace were unmatched, and observers described her as seeming to glide above the earth with each step. She often challenged others to wager on her speed, but as people began to grow wise, she was forced to conceal her identity or promise to forfeit her sandals if she lost. These sandals give you a +1 item bonus to Athletics checks to [[High Jump]] and [[Long Jump]]. In addition, when you use the [[Leap]] action, you can move 5 feet further if jumping horizontally or 3 feet higher if jumping vertically.

**Activate—Light-Footed Bound** `pf2:2` (concentrate)

**Frequency** once per hour

**Effect** You loudly boast about your grace and agility, then take any combination of two High Jumps or Long Jumps. You don't need to Stride first, and between the two jumps, you need only to come into contact with a physical object before making the second jump; this object doesn't need to be one that can bear your weight, or even be attached to the ground—you can jump off of a floating feather or a thin branch or even off a paper wall as needed. The sandals' item bonus increases to +2 for these jumps.

**Source:** `= this.source` (`= this.source-type`)
