---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Cursed]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 30}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This elegant scarf appears to be and functions as a [[Masquerade Scarf]]. When you invest the scarf, it fuses to you.

**Activate** 1 minute (manipulate)

**Frequency** once per day

**Effect** Like a masquerade scarf, the scarf casts a 1st-rank [[Illusory Disguise]] spell on you. However, the illusion disadvantages you based on your intent, making you, for example, appear to be a suspicious ruffian if you're trying to sneak past guards or lending you the seeming of a pauper if you're trying to impress a shallow aristocrat. You and those you consider to be allies must succeed at a DC 16 [[Will]] save or you perceive the illusion as you intended it, though others won't. Evidence to the contrary allows you to attempt to disbelieve the false version of the illusion. You can't Dismiss the spell.

**Source:** `= this.source` (`= this.source-type`)
