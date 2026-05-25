---
type: creature
group: ["Aberration", "Amphibious"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Grindylow"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Aberration"
trait_02: "Amphibious"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Darkvision]]"
languages: "Thalassic"
skills:
  - name: Skills
    desc: "Athletics +5, Stealth +7, Survival +5"
abilityMods: ["+1", "+3", "+2", "-1", "+3", "+0"]
abilities_top:
  - name: "Clinging Suckers"
    desc: "When a grindylow successfully Grabs a creature larger than themself, they attach to that creature. The [[Grabbed]] creature is not [[Immobilized]], but if it moves, the grindylow moves with it. <br>  <br> If the creature is Medium or smaller, it takes a –5-foot status penalty to its Speeds while the grindylow is attached. The grindylow is [[Off Guard]] while attached to a creature."
armorclass:
  - name: AC
    desc: "15; **Fort** +6, **Ref** +7, **Will** +5"
health:
  - name: HP
    desc: "14"
abilities_mid:
  - name: "Reactive Strike (Special)"
    desc: "`pf2:r` A grindylow gains 1 extra reaction at the start of each of their turns that they can use only to make a Reactive Strike with a tentacle. They can't use more than one Reactive Strike triggered by the same action or choice. <br>  <br> **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bite +7 (`pf2:1`) (finesse), **Damage** 1d6+1 piercing"
  - name: "Melee strike"
    desc: "Tentacle +7 (`pf2:1`) (agile, finesse, trip, unarmed), **Damage** 1d4+1 bludgeoning plus [[Grab]]"
  - name: "Melee strike"
    desc: "Spear +5 (`pf2:1`), **Damage** 1d6+1 piercing"
  - name: "Melee strike"
    desc: "Spear +7 (`pf2:1`) (thrown 20), **Damage** 1d6+1 piercing"
spellcasting: []
abilities_bot:
  - name: "Jet"
    desc: "`pf2:2` The grindylow moves up to 60 feet in a straight line through the water without triggering reactions."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The top half of a grindylow vaguely resembles a goblin, but from the waist down, their bodies split into a tangle of suckered, wriggling tentacles. Grindylows mostly dwell in shallow waters, fresh and briny, including lakes, rivers, coastal regions, and coral reefs. They generally organize into groups called schools, which can range from a few individuals to a few hundred. Smaller schools are sometimes taken over by a powerful aquatic creature, though such alliances only last until the school faces a major setback, at which point the surviving grindylows scatter and form smaller schools of their own.

Grindylows aren't territorial, but they are pragmatic. While they rarely build permanent structures, they will adopt a good hunting ground for generations until driven away by predators. They often lair in mobile shelters, such as a sargasso of seaweed or hull of an abandoned ship. They are skilled scavengers and hunters who eat anything they can sink their teeth into.

Grindylows respect the power of larger sea predators but have a special hatred for squids (or anything that resembles a squid). Sailors plying grindylow-infested waters often paint the images of squids on the bottoms of their hulls in hopes of warding off potentials raids. While this can keep smaller schools at bay, it can also backfire, potentially inciting larger groups to gather for a coordinated attack; this becomes especially likely if the ship's route is predictable. Their hatred of squids does not extend to other tentacled creatures; grindylows consider octopuses to be the epitome of grace and power.

```statblock
creature: "Grindylow"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
