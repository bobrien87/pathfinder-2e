---
type: item
source-type: "Remaster"
level: "8"
price: "{'gp': 487}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Druids and Calistria's faithful alike value this vindictive armor for its ability to turn away pests and exact revenge on foes in a manner that can easily turn coordinated enemies into a chaotic mass. *Wasp guard* is *+1 studded leather* studded with the carapaces of wasps, subtly diverting swarms away and granting a +1 status bonus to Reflex saving throws against Swarming Bites, Swarming Stings, and similar abilities from swarms.

**Activate** R (concentrate)

**Frequency** once per day

**Trigger** An enemy within 30 feet Strikes you with an attack

**Effect** You animate the exoskeletons of the *wasp guard* armor into a spectral swarm of wasps that seeks revenge for the slight. The swarm flies to the triggering enemy's space and swarms about them, dealing 1d8 persistent,poison damage. If the affected enemy has any allies within 30 feet, the enemy can spend a single action, which has the manipulate trait, to shoo the swarm away. This ends the persistent damage on that enemy automatically, but the swarm instead moves to affect the enemy's ally.

**Craft Requirements** The initial raw materials must include 1 Bulk of wasp exoskeletons.

**Source:** `= this.source` (`= this.source-type`)
