---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Divine]]", "[[Holy]]", "[[Talisman]]"]
price: "{'gp': 10}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You Stride.

These strips of supple leather, typically about 2 inches wide and 3 feet long, feature sigils, runes, and divine marks that reflect family lineage and beliefs in the old gods of Sarkoris. When activated, the band's holy patterns surround you as you move, preventing your movement from triggering reactions from demons. The holy patterns scour nearby demons; any demons you pass adjacent to during the triggering movement take damage equal to their weakness to holy effects. You can activate the bands when you Burrow, Climb, Fly, or Swim (instead of Stride) if you have the corresponding movement type.

**Source:** `= this.source` (`= this.source-type`)
