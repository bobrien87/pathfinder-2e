---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 350}"
usage: "worn"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This glass amulet is set on a steel backing shaped like a cage and flickers with an eerie crimson glow. Magically sealed within is a portion of a hellcat's ever-burning heart. While wearing the amulet, you gain a +1 item bonus to Stealth checks made while in bright light, and you can cast the [[Light]] cantrip emanating from the amulet as an innate divine spell.

**Activate—Invisible Pounce** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Requirements** You are in bright light

**Effect** You become [[Invisible]], Stride up to your speed, and then make a melee Strike at the end of that movement. After making the Strike, you are no longer invisible. If at any point during your Stride, you pass out of bright light, you are no longer invisible and must stop moving. You may make a melee Strike if you have a target within reach.

**Craft Requirements** The initial raw materials must include the heart of a hellcat.

**Source:** `= this.source` (`= this.source-type`)
