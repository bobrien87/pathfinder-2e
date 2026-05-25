---
type: creature
group: ["Amphibious", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mist Stalker"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Amphibious"
trait_02: "Elemental"
trait_03: "Water"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Darkvision]]"
languages: "Thalassic"
skills:
  - name: Skills
    desc: "Athletics +10, Stealth +12"
abilityMods: ["+4", "+4", "+2", "+1", "+5", "+0"]
abilities_top:
  - name: "Mist Vision"
    desc: "The mist stalker ignores the [[Concealed]] condition from mist and fog."
armorclass:
  - name: AC
    desc: "20; **Fort** +10, **Ref** +12, **Will** +11"
health:
  - name: HP
    desc: "60; **Immunities** bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Mist Cloud"
    desc: "15 feet. The mist stalker is surrounded by mist. Creatures in the aura are [[Concealed]]. If wind disperses the aura, it returns automatically at the start of the mist stalker's turn. This cloud is suppressed in water."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tentacle +14 (`pf2:1`) (finesse, reach 10 ft., sweep), **Damage** 2d8+4 bludgeoning plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(1d8+4)[bludgeoning]] damage, DC 21 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Solidify Mist"
    desc: "`pf2:1` The mist stalker makes its mist cloud congeal, causing the aura to be difficult terrain until the start of the mist stalker's next turn. In addition, the mist stalker can make the mist even thicker around a single Medium or smaller creature within the cloud. The creature must succeed at a DC 20 [[Reflex]] save or become [[Immobilized]] until it Escapes or is no longer in the mist cloud's emanation."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The tentacled mist stalker shrouds itself in a cloak of mist through which its single, never-blinking eye can see with clarity, allowing it an advantage when stalking prey.

Water elementals that become infused with cold or mist have increased mobility in regions outside of bodies of water.

```statblock
creature: "Mist Stalker"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
