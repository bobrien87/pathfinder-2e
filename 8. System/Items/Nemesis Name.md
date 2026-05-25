---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 650}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You want revenge badly enough that you tattoo your nemesis's name in a place you can easily see to remember your vow to settle the score. Anyone who sees the tattoo senses your hatred of the named being. Receiving a new nemesis name makes any you already have non-magical. You gain a +2 status bonus to damage rolls against the creature named on your tattoo, but this nemesis gains a +1 status bonus to damage rolls against you.

**Activate** `pf2:1` (concentrate, mental)

**Frequency** once per round

**Requirements** You can see your nemesis, and they're within 30 feet of you

**Effect** You focus your hatred into a mental scream. Your nemesis takes 3d6 mental damage, which they can resist with a DC 26 [[Will]] save. You take half as much damage as your nemesis does, and you can't reduce this damage in any way.

**Source:** `= this.source` (`= this.source-type`)
