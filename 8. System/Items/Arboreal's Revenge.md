---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Concussive]]", "[[Cursed]]", "[[Magical]]", "[[Scatter 10]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This walnut and brass *+1 striking blunderbuss* has a natural look, with wood worn smooth by time, but left knotted and gnarled. The handgrip beneath the flared muzzle is a well-positioned bulging tree knot, and the long stock looks as if it was grown to fit you. On closer examination, the whorls and rings in the wood resemble eyes.

*Arboreal's revenge* is a haunted firearm constructed with wood hewn from a living arboreal, slaying the arboreal and trapping its spirit in the firearm. Perhaps a patient wielder could one day put the arboreal's spirit to rest, or at least come to terms with it, abating the drawbacks of the weapon while keeping its advantages.

When you first fire *arboreal's revenge*, the blunderbuss fuses with you, after which it's almost impossible to remove it from your possession with a [[Cleanse Affliction]] or similar effect, like many cursed items. You gain weakness 5 to fire and the flat check for you to recover from persistent fire damage increases from 15 to 17, or from 10 to 12 if you receive appropriate help.

Whenever you wield *arboreal's revenge*, the arboreal spirit bound to the blunderbuss attempts to overtake you. The wood handgrip sprouts roots which grow around your hand, binding both of your hands to the firearm. You gain a +4 circumstance bonus to your Reflex DC when defending against checks to [[Disarm]] you. However, you can't Release your grip on the blunderbuss until you forcibly tear off the roots, though they do allow you to move your hands enough (and only enough) to reload and fire the blunderbuss. Tearing off the roots takes 1 minute.

The arboreal haunting the firearm can use the following two effects whenever it wants, often using them at random. You can coax it into performing them each intentionally once per day, with the following activations.

**Activate—Arboreal Growth** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** The arboreal haunting the blunderbuss attempts to regrow itself into a new physical body by sprouting from the bodies of all the creatures that the firearm recently harmed. You and all creatures within 60 feet damaged by *arboreal's revenge* within the last minute must attempt a [[Fortitude]] save saving throw. On a failure, they take a –10-foot circumstance penalty to their Speeds as roots rapidly sprout from their wounds, which lasts until they `act escape show-dc=all dc=20`.

> [!danger] Effect: Arboreal's Revenge (Speed Penalty)

**Activate—Arboreal's Grace** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You cast [[Oaken Resilience]] from the blunderbuss as a 2nd-rank primal spell. However, the weakness to fire imposed by oaken resilience is cumulative with the weakness to fire imposed by this weapon's curse, for a total of weakness 8 to fire.

> [!danger] Effect: Spell Effect: Oaken Resilience (Arboreal's Revenge)

**Source:** `= this.source` (`= this.source-type`)
