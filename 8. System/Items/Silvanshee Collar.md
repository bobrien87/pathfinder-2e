---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Apex]]", "[[Holy]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 40000}"
usage: "worn"
bulk: "L"
source: "Pathfinder #206: Bring the House Down"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *silvanshee collar* appears as a collar of prismatic cloth affixed with a tiny bell, but once worn on the body or affixed to your hair, a Tiny cat wearing a similar (but non-magical) collar appears at your feet. This cat is similar to a silvanshee agathion, but its stats are determined as if you gained the [[Pet]] general feat. When you first invest the collar, you must name your silvanshee pet, then build its statistics as detailed in the Pet general feat. The silvanshee has a name (chosen by you) and a unique personality. Whenever you invest the same *silvanshee collar*, the silvanshee who appears is the same one you named and chose the first time. If you already have a pet, familiar, or other companion that uses the Pet feat, that pet can change its shape as an action to appear as a silvanshee agathion at will (while perhaps retaining some of your pet's cosmetic traits at your option), but this doesn't otherwise alter your existing pet's statistics.

As long as you wear the *silvanshee collar*, you gain a +3 item bonus to Performance checks and a +2 circumstance bonus to Gather Information. When you invest it, you either increase your Charisma modifier by 1 or increase it to +4, whichever would give you a higher value. If you are unholy, you become [[Clumsy]] 2 as long as you wear the collar.

**Activate—Awww!** `pf2:r` (concentrate, fortune, visual)

**Frequency** once per hour

**Trigger** You fail on an attempt to Lie or [[Make an Impression]]

**Requirements** Your pet can observe you

**Effect** Your pet does something distracting or adorable at the precise moment you failed, allowing you to reroll the failed check and to use the result of your choice as the actual result.

**Source:** `= this.source` (`= this.source-type`)
