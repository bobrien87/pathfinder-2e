---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Evil]]"]
price: "{'gp': 250}"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Those favored by Asmodeus can be found wearing this *+1 studded leather*, which is lacquered in red and black.

**Activate** `pf2:r` (concentrate, fortune)

**Frequency** once per day

**Trigger** You critically fail an attack roll, check, or saving throw

**Effect** You offer a prayer to Asmodeus, who accepts under a reciprocal condition. Reroll the triggering roll with a +2 circumstance bonus and use the higher result.

If this reroll improves your degree of success, the GM can later reroll one Strike against you, one saving throw against your abilities, or one secret check or saving throw you make. This is a fortune effect if used on a Strike or save against you, or a misfortune effect if used on your secret check or saving throw. The GM must use this reroll before the end of the last day you activated the armor.

**Source:** `= this.source` (`= this.source-type`)
