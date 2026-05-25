---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 900}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ostentatious hat is trimmed with gold thread and tiny jewels, all proclaiming your position of authority on the high seas. While wearing the bicorne, you gain a +2 item bonus to Intimidation and Sailing Lore checks.

**Activate—Fight On** `pf2:r` (concentrate)

**Frequency** once per day

**Trigger** You take damage from an enemy's Strike or spell attack roll

**Effect** Despite your wounds, your troops are inspired to fight on. For 1 minute, all allies in a @Template[type:emanation|distance:30] gain a +2 status bonus to saving throws against fear effects.

> [!danger] Effect: Fight On

**Source:** `= this.source` (`= this.source-type`)
