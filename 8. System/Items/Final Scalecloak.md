---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Artifact]]", "[[Invested]]", "[[Magical]]", "[[Mythic]]"]
price: "{'value': {}}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Fashioned from a swath of Mogaru's red-and-black hide and trimmed with Agyra's rough scales in green, blue, and white, this cloak draws upon the power of both kaiju, but at considerable cost. Any kaiju within a 5-mile radius of the *Final Scalecloak* can sense the presence and nature of the item, and can also determine whether it's being worn by a mortal. This sense grows stronger as the item and kaiju near one another, until the kaiju can pinpoint exactly where the cloak is and who currently possesses it.

When worn, the *Final Scalecloak* grants you resistance 15 to physical and precision damage, immunity to electricity, and a Fly speed of 60 feet. You are unaffected by strong winds while flying.

**Activate—Commune with Kaiju** `pf2:2` (concentrate, manipulate, primal)

**Frequency** once per day

**Effect** Spend a Mythic Point; you gain the effects of a 6th-rank [[Telepathy]] spell but can use it only to communicate with Gargantuan animals and beasts. Most kaiju are hostile toward you for wearing the *Final Scalecloak*, however, requiring great effort to calm them enough to have a conversation.

**Activate—Embody the Storm** `pf2:2` (concentrate, manipulate, primal)

**Frequency** once per hour

**Effect** Spend a Mythic Point; a nimbus of crackling electricity surrounds you for 1 minute. You gain a +4 status bonus to AC against ranged projectiles that are at least partly made of metal. If a foe attempts to Strike you with an unarmed attack or melee attack with a weapon at least partly made of metal, that creature takes 3d10 electricity damage (DC 40 [[Reflex]] save).

> [!danger] Effect: Embody the Storm

**Destruction** The *Final Scalecloak* is torn to shreds if the wearer is struck by an attack or effect from both Agyra and Mogaru within the same round.

**Source:** `= this.source` (`= this.source-type`)
