---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Focused]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 2000}"
usage: "worngarment"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Each *bloodline robe* has a design that befits a particular sorcerer bloodline, depicting creatures of that bloodline or using styles common among them. You gain a +2 item bonus to each of your bloodline skills.

**Activate** `pf2:1` (concentrate)

**Frequency** once per day

**Requirements** You're benefiting from your blood magic effect or gained its benefit earlier this turn

**Effect** You're [[Quickened]] on your next turn. You can use the extra action only as part of casting a bloodline spell.

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can use only to cast a sorcerer bloodline spell. If not used by the end of your turn, this Focus Point is lost.

**Craft Requirements** You are a sorcerer of the bloodline tied to the robe.

**Source:** `= this.source` (`= this.source-type`)
