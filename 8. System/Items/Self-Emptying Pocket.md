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

You never perform to an empty crowd after promising any profits to a phantom in a playhouse, sealed by holes that appear in your pockets. By meeting with the attendees at your events, you can use Performance instead of Diplomacy to Gather Information. When you would use Performance to [[Earn Income]], you don't earn any gold pieces, as the money disappears before you can even count it.

The entity that holds your *bargained contract* can influence your reception any time you perform for a crowd or Activate the pocket. If they influence your performance favorably, you gain a +2 item bonus to your Performance check. If they influence your performance unfavorably, you take a -2 item penalty to your Performance check. If you've failed to earn the entity money in quite a while, it often influences your performance unfavorably.

**Activate—Beguiling Presence** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** You exercise all of your charm on a creature, turning a chance meeting into an impromptu performance that commands attention. Attempt a single Performance check against the Perception DC of the creature. On a success, the creature is affected as though by a successful Deception check to `act create-a-diversion`. The entity that holds your contract can influence this performance as well.

**Source:** `= this.source` (`= this.source-type`)
