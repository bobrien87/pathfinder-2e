---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Consumable]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'cp': 0, 'gp': 5000, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *key of unwinding* is a narrow brass clock hand, its pointed end fashioned into the shape of a key. When applied to a weapon, a *key of unwinding* forms a direct link to the Dimension of Time, allowing you to draw on a fragment of temporal power. For 1 minute, you gain the Rewrite Time reaction while wielding the attuned weapon.

**Rewrite Time** R (magical, occult)

**Trigger** You or an ally within your weapon's reach or range increment would be hit by a Strike or a spell attack roll

**Effect** Attempt a Strike with the affected weapon against the triggering enemy. On a success, you deal no damage, but you negate the triggering attack or spell. Actions and spell slots used to attempt this attack are lost, and the triggering creature's multiple attack penalty increases as normal, as the results of the action are siphoned into the Dimension of Time. Any creature attempting to use Rewrite Time more than once per combat becomes [[Slowed]] 1 for 1 round after each subsequent use, as their own time begins to leech away.

**Source:** `= this.source` (`= this.source-type`)
