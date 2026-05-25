---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Contract]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Your very quintessence has been hijacked by the agony of Dahak that lingered within your bound dragon. The wracked god's whispers burn your soul and ride your body to work in dire concordance with his whims. You are the very face of horror, an heir of the Dragon Plague's rancor, the Endless Destruction made manifest in an overwhelmed mortal form. You gain the Scream of Unending Destruction activity. In exchange, the dragon who bound you to this pact is now free from the influences of Dahak, losing any boons or abilities that might have been granted if they were a follower of Dahak and gaining a +2 item bonus on saving throws against any spells or abilities cast by followers of Dahak.

**Scream of Unending Destruction** `pf2:2` (auditory, concentrate, emotion, fear, incapacitation, mental, unholy)

**Frequency** once per day

**Effect** Attempt an Intimidation check against the Will DC of each creature in a @Template[type:emanation|distance:30] that you observe and that observes you.
- **Critical Success** The target must attempt a Fortitude save against your Intimidation DC. On a critical failure, it dies in an explosion of hellfire that deals @Damage[6d6[fire]|options:area-damage] damage to each creature in a @Template[type:emanation|distance:5]. On any other result, the creature becomes [[Frightened]] 3 and is [[Fleeing]] for 1 round. The critical failure effect has the death trait.
- **Success** The target becomes frightened 3 and takes @Damage[4d6[fire]|options:area-damage] damage.
- **Failure** The target becomes [[Frightened]] 2.
- **Failure** The target is unaffected.

**Oathbreaker's Calamity** The souls of both parties begin to become consumed by the agony of Dahak. At the end of each day, you and your dragon become [[Doomed]] 1 (or increase your doomed values by 1 if you're already doomed) unless both of you acted in service to Dahak that day. If you or your bound dragon die while under this effect, both of you explode in a catastrophe of hellfire and pitch, dealing @Damage[16d6[fire]|options:area-damage] damage to all creatures in a @Template[type:emanation|distance:30]; this effect has the divine and unholy traits. If the creature who didn't die also survives this blast, the pact of the agonized destroyer ends.

**Source:** `= this.source` (`= this.source-type`)
