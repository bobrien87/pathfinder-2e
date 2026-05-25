---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]"]
price: "{'gp': 1150}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #209: Destroyer's Doom"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This thin, wand-like implement is carved from bone and scrimshawed with depictions of battle. While holding the *needle of undeath*, mindless undead creatures see you as one of their own and are indifferent to you until you take hostile actions against them, and you have a +2 item bonus to Deception and Diplomacy checks against intelligent undead. This does not affect a summoned undead's attitude.

**Activate—Speak with Undead** `pf2:1`

**Frequency** once per hour

**Effect** You can use Diplomacy to [[Make an Impression]] on mindless undead or make simple requests of them with a +2 item bonus. You cannot make this request of someone else's summoned undead.

**Source:** `= this.source` (`= this.source-type`)
