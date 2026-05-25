---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 13000}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Crafters choose tattoos that represent their dedication and skill in their chosen field. Such tattoos might adorn the arm, fingers, or eyes, and they take the form of artistic patterns or depict tools of the trade, such as anvils, paintbrushes, or trowels. You gain a +3 item bonus to Crafting checks. Furthermore, when you roll a critical failure on a Crafting check to [[Earn Income]], treat it as a failure instead.

**Activate** 1 minute (concentrate, manipulate)

**Frequency** once per day

**Effect** The tattoo casts [[Creation]]. You choose the item and its appearance, and whether the spell is 4th or 5th rank. This spell's duration is unlimited but ends when you Activate the tattoo again.

**Source:** `= this.source` (`= this.source-type`)
