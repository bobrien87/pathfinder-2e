---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Contract]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "other"
bulk: "—"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Whether due to the inconvenience of having a physical body or the desperation of impending starvation, you were drawn to a person offering relief from hunger. You swallowed a key, which remains in your stomach, that continuously satiates you. You no longer need to eat or drink. Once per day, from any distance, the entity that holds your *bargained contract* can have the key sealing your *bargained contract* absorb all items in your stomach, which prevents you from benefiting from items that require you to eat or drink them, such as potions and elixirs, for 10 minutes. During this time, the entity gains the benefits of these items instead.

**Activate—Iron Gut** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** You absorb any poisons with the key sealing your *bargained contract*. You're affected by a 5th-rank [[Cleanse Affliction]] spell to remove a poison (counteract modifier +15).

**Source:** `= this.source` (`= this.source-type`)
