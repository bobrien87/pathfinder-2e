---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Fire]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 350}"
usage: "wornclothing"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*Ash gowns* are formal wear spun from smoke, ash, and char collected from the Plane of Fire. Typically, they're voluminous floor-length dresses or three-piece suits, but regardless of their specific tailoring, *ash gowns* are always an ostentatious display of wealth and loyalty to the powers of the Plane of Fire. They're exceptionally popular in the courts of the Elemental Lords and among the high society of Medina Mudii'a. The gown grants you resistance 5 to fire and a +1 item bonus to Intimidation checks.

**Activate—Blazing Promenade** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** The *ash gown* ignites in a ferocious blaze, flames licking the floor and trailing behind you like a dancing cape. You Stride and make a Strike at the end of your movement. During the Stride, your flames incinerate minor obstacles in your path; you ignore non-magical difficult terrain, and any you move through is destroyed. Creatures that are adjacent to you at any point during your movement take 2d6 fire damage with a DC 23 [[Reflex]] save. A creature doesn't need to attempt this save more than once, even if you move past it multiple times.

**Source:** `= this.source` (`= this.source-type`)
