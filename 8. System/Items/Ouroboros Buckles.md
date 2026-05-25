---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Adjusted]]", "[[Comfort]]"]
price: "{'gp': 40000}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ominous-looking *+3 greater resilient greater acid-resistant buckle armor* is deep red in color, favored by assassins who worship Norgorber or Asmodeus, and if unfastened, the many belts and buckles writhe like living snakes. Its form and abilities were inspired by ouroboros, embodiments of eternity that continually consume and regenerate their bodies and appear to be formed from masses of snakes. *Ouroboros buckles* have the comfort trait. However, while wearing *ouroboros buckles*, the unfathomable concept of infinity pulls at your mind, and each time you awaken, you'd swear the armor hissed into your ear while you were asleep. The hissing suggested secret wisdom to you in Aklo, though you only ever remember it vaguely, like a fading dream.

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You call forth the cursed regenerative blood of an ouroboros to recover from your wounds. You gain regeneration 15 for 1 minute; fire damage deactivates this regeneration. Each time you regain Hit Points from this regeneration, if you're in your normal form, you collapse into a Large swarm of Tiny snakes. This is a polymorph effect that changes you into a battle form.

When you're a swarm of snakes, you gain low-light vision, imprecise scent (30 feet), a Speed of 20 feet, a climb Speed of 20 feet, and a swim Speed of 20 feet. You have an AC of 16 + your level and ignore your armor's check penalty and Speed reduction. Also, you gain resistance 5 to physical damage and weakness 5 to area damage and splash damage. You can use none of your normal Strikes. Instead, you can use Swarming Bites, a single action that deals @Damage[4d4[piercing],2d6[poison]|options:area-damage] damage to creatures in your space with a DC 41 [[Reflex]] save.

If you're in this battle form and are already at full HP when your regeneration occurs, the snakes instantaneously slither together, and you transform into your original form.

> [!danger] Effect: Ouroboros Buckles

> [!danger] Effect: Ouroboros Buckles (Swarm of Snakes)

**Activate** R (concentrate)

**Frequency** once per minute

**Trigger** A foe within 15 feet hits you with a Strike that deals slashing or piercing damage

**Effect** Your *ouroboros buckles* spray acidic blood in a @Template[cone|distance:15] toward the foe, dealing @Damage[5d6[acid]|options:area-damage] damage with a DC 41 [[Reflex]] save.

**Source:** `= this.source` (`= this.source-type`)
