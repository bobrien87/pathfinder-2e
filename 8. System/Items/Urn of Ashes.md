---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]", "[[Void]]"]
price: "{'gp': 700}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This sealed pewter urn contains the ashes of a benevolent ancestor, with a sliver of lingering spirit that strives to protect you.

**Activate—Doom the Urn** `pf2:r` (concentrate)

**Trigger** You would become [[Doomed]], or your doomed value would increase

**Requirements** The ashes aren't doomed

**Effect** The ashes in the urn intervene, taking the doomed condition in your place, and you don't gain or increase the value of your doomed condition. Each night when you get a full night's rest, you can reduce your own doomed condition or that of the urn, but not both.

**Activate—Spirit's Wrath** `pf2:1` (attack, concentrate, manipulate)

**Frequency** once per round

**Effect** The urn shoots a bolt of void energy at a foe within 30 feet. Attempt a spell attack roll against the target's AC, using a modifier of +15 or your own spell attack modifier, whichever is higher. On a success, the bolt deals 4d4 void damage (doubled on a critical success).

**Source:** `= this.source` (`= this.source-type`)
