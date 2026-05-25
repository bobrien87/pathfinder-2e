---
type: creature
group: ["Mindless", "Ooze"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Living Tar"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Mindless"
trait_02: "Ooze"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Motion Sense]] (precise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +18"
abilityMods: ["+7", "-5", "+7", "-5", "+0", "-5"]
abilities_top:
  - name: "Motion Sense"
    desc: "A living tar can feel nearby motion through vibration and air movement."
armorclass:
  - name: AC
    desc: "14; **Fort** +18, **Ref** +6, **Will** +11"
health:
  - name: HP
    desc: "165; **Immunities** acid, bleed, bludgeoning, critical hits, mental, precision, unconscious, visual"
abilities_mid:
  - name: "Adhesive Mass"
    desc: "A weapon that hits the living tar is stuck to the ooze. Removing it requires a successful DC 23 [[Athletics]] check to Break Open. The living tar can have any number of objects or creatures stuck to it at a time. <br>  <br> It can release a stuck object with an Interact action, and the adhesive dissolves 1 minute after the ooze dies, releasing all stuck objects and creatures."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pseudopod +18 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d6 acid plus 2d8+7 bludgeoning plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(1d8+7)[bludgeoning],1d6[acid]], DC 26 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Engulf"
    desc: "`pf2:2` DC 22 [[Reflex]] save, @Damage[(4d6)[acid]] damage, `act escape dc=22`, Rupture 15 <br>  <br> The monster Strides up to double its Speed and can move through the spaces of any creatures in its path. Any creature of the monster's size or smaller whose space the monster moves through can attempt a Reflex save with the listed DC to avoid being engulfed. A creature unable to act automatically critically fails this save. If a creature succeeds at its save, it can choose to be either pushed aside (out of the monster's path) or pushed in front of the monster to the end of the monster's movement. The monster can attempt to Engulf the same creature only once in a single use of Engulf. The monster can contain as many creatures as can fit in its space. <br>  <br> A creature that fails its save is pulled into the monster's body. It is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The creature takes the listed amount of damage when first engulfed and at the end of each of its turns while it's engulfed. An engulfed creature can get free by [[Escaping]] against the listed escape DC. An engulfed creature can attack the monster engulfing it, but only with unarmed attacks or with weapons of light Bulk or less. The engulfing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the engulfed creature cuts itself free. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> A creature that gets free by either method can immediately breathe and exits the swallowing monster's space. <br>  <br> If the monster dies, all creatures it has engulfed are automatically released as the monster's form loses cohesion."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Most often found belowground, these oozes scour caves for objects to dissolve with their corrosive secretions. These sticky masses are often filled with bones, fossils, and discarded weaponry from adventurers.

Slimes, molds, and other oozes can be found in dank dungeons and shadowed forests. While not necessarily evil, some grow to enormous sizes and have insatiable appetites.

```statblock
creature: "Living Tar"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
