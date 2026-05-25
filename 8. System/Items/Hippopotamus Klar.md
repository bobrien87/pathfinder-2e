---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Integrated 1d6 s versatile p]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 1000}"
bulk: "1"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking klar* is fashioned from the skull of a hippopotamus, with one of its canines acting as the blade. While wielding a *hippopotamus klar*, you gain a +1 item bonus to Intimidation checks.

**Activate—Engulfing Jaws** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** The hippo jaws of the shield open impossibly wide. Make a melee Strike with the klar blade targeting two creatures adjacent to each other. Roll the attack and damage once and apply it to each creature separately. This counts as two attacks for your multiple attack penalty.

**Craft Requirements** The initial raw materials must include the entire skull of a hippopotamus.

**Source:** `= this.source` (`= this.source-type`)
