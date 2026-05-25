---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 350}"
usage: "worn"
bulk: "—"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

While the Kalistocrats of Druma profiteer off selling weapons to both Hellbreakers and Hellknights, they also offer options suitable for intelligence and counterintelligence efforts. This white gold ring grants you a +1 item bonus to skill checks to Decipher Writing that's primarily numerical or mathematical in nature as well as to skill checks to [[Make an Impression]] and [[Coerce]] to convince others of the fairness or accuracy of your judgments.

**Activate—Fair Assessment** `pf2:2` (concentrate, manipulate, mental)

**Frequency** once per hour

**Effect** The Prophecies of Kalistrade reveal the secrets of wealth to you; this appears as a balance sheet of numbers only you can see. Choose an area of up to 1 cubic foot within 30 feet; you can estimate the value in gold pieces of any items within this area. If you attempt to estimate the value of items worn or held by a creature, you must succeed at a Society check to Decipher Writing against their Will DC.

**Source:** `= this.source` (`= this.source-type`)
