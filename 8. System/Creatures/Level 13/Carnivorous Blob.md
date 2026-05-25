---
type: creature
group: ["Mindless", "Ooze"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Carnivorous Blob"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Mindless"
trait_02: "Ooze"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+23; [[Motion Sense]] (precise) 240 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +27"
abilityMods: ["+8", "-3", "+6", "-5", "+0", "-5"]
abilities_top:
  - name: "Motion Sense"
    desc: "A carnivorous blob can sense nearby creatures through vibration and air or water movement."
  - name: "Carnivorous Blob Acid"
    desc: "A carnivorous blob's acid damages only flesh-not bone, stone, wood, or other materials- but is nonetheless devastating. Whenever a creature takes damage from this acid, it must succeed at a DC 33 [[Fortitude]] save or become [[Drained]] 1 (drained 2 on a critical failure). On each subsequent failure, the drained condition value increases by 1 (or by 2 on a critical failure), to a maximum of drained 4."
armorclass:
  - name: AC
    desc: "20; **Fort** +25, **Ref** +14, **Will** +19"
health:
  - name: HP
    desc: "300; **Immunities** acid, critical hits, piercing, precision, slashing, sonic, unconscious, visual"
abilities_mid:
  - name: "Retaliating Strike"
    desc: "`pf2:r` **Trigger** The carnivorous blob takes damage from any source <br>  <br> **Effect** The blob makes a pseudopod Strike against an adjacent target. If an adjacent creature dealt the triggering damage, that creature is the target of this Retaliating Strike."
  - name: "Split"
    desc: "When a carniverous blob that has 10 or more HP is hit by an attack that would deal piercing or slashing damage, it splits into two identical oozes, each with half the original's HP. One ooze is in the same space as the original, and the other is in an adjacent, unoccupied space. If no adjacent space is unoccupied, it automatically pushes creatures and objects out of the way to fill a space (the GM decides if an object or creature is too big or heavy to push)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pseudopod +25 (`pf2:1`) (reach 30 ft., unarmed), **Damage** 2d12+12 bludgeoning plus 2d6 acid plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[2d12[bludgeoning],2d6[acid]]{2d12 bludgeoning plus 2d6 acid}, DC 33 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Engulf"
    desc: "`pf2:2` DC 33, 4d10 acid damage, `act escape dc=33`, Rupture 20 <br>  <br> The monster Strides up to double its Speed and can move through the spaces of any creatures in its path. Any creature of the monster's size or smaller whose space the monster moves through can attempt a Reflex save with the listed DC to avoid being engulfed. A creature unable to act automatically critically fails this save. If a creature succeeds at its save, it can choose to be either pushed aside (out of the monster's path) or pushed in front of the monster to the end of the monster's movement. The monster can attempt to Engulf the same creature only once in a single use of Engulf. The monster can contain as many creatures as can fit in its space. <br>  <br> A creature that fails its save is pulled into the monster's body. It is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The creature takes the listed amount of damage when first engulfed and at the end of each of its turns while it's engulfed. An engulfed creature can get free by [[Escaping]] against the listed escape DC. An engulfed creature can attack the monster engulfing it, but only with unarmed attacks or with weapons of light Bulk or less. The engulfing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the engulfed creature cuts itself free. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> A creature that gets free by either method can immediately breathe and exits the swallowing monster's space. <br>  <br> If the monster dies, all creatures it has engulfed are automatically released as the monster's form loses cohesion."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Carnivorous blobs are the ravenous spawn of shattered worlds far beyond the stars, born across the galaxy in inert form until they fall like meteorites onto unsuspecting worlds. These massive beings can lie dormant for years in desolate caverns or barren wastelands. When a carnivorous blob perceives living creatures nearby, it lurches to gelatinous life, seeking out and consuming every creature it can catch until it is destroyed or until it has been unable to locate food for 24 hours, at which point it returns to hibernation. Often, keeping food away from a carnivorous blob is the safest way to defeat it. The blob's ability to split into smaller oozes that might stay hidden after a fight means it can be hard to fully eradicate these mindless predators.

```statblock
creature: "Carnivorous Blob"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
