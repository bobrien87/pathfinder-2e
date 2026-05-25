---
type: item
source-type: "Remaster"
level: "21"
traits: ["[[Artifact]]", "[[Divine]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "worneyepiece"
bulk: "—"
source: "Pathfinder #206: Bring the House Down"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Delicate engravings of spiders and cleomes decorate the silver cover of this magnifying loupe.

Anything viewed through these thin spectacles looks crisp and clear, and the earpieces accentuate sounds around you. You gain a +3 item bonus to Perception checks.

**Activate** `pf2:1` envision

**Frequency** once per hour

**Effect** The spectacles key in on someone to show you their social cues in perfect clarity. Choose a creature you can see. You gain a +4 item bonus on Perception checks you make to use [[Sense Motive]] against that creature. This benefit lasts until you Activate the item again in this way. If you're an investigator, you can use this activation as part of the action you take to [[Devise a Stratagem]] or [[Pursue a Lead]], and you can do the latter even though you can't see the creature. You must choose the same creature you chose for Devise a Stratagem or Pursue a Lead.

**Source:** `= this.source` (`= this.source-type`)
