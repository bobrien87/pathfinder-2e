---
type: creature
group: ["Humanoid", "Kobold"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kobold Cavern Mage"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Humanoid"
trait_02: "Kobold"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Darkvision]]"
languages: "Common, Fey, Petran, Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +6, Deception +8, Diplomacy +8, Intimidation +8, Nature +5, Stealth +6"
abilityMods: ["+2", "+2", "-1", "+0", "+1", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "16; **Fort** +5, **Ref** +6, **Will** +7"
health:
  - name: HP
    desc: "20; **Resistances** cold 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +6 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d6+2 slashing"
  - name: "Melee strike"
    desc: "Light Hammer +6 (`pf2:1`) (agile), **Damage** 1d6+2 bludgeoning"
  - name: "Melee strike"
    desc: "Light Hammer +6 (`pf2:1`) (agile, thrown 20), **Damage** 1d6+2 bludgeoning"
spellcasting:
  - name: "Primal Spontaneous Spells"
    desc: "DC 18, attack +10<br>**1st** (4 slots) [[Caustic Blast]], [[Detect Magic]], [[Figment]], [[Fleet Step]], [[Heal]], [[Know the Way]], [[Pummeling Rubble]], [[Runic Weapon]], [[Tangle Vine]]"
abilities_bot:
  - name: "Inspiring Display"
    desc: "`pf2:1` **Requirements** The cavern mage's previous action was to Cast a Spell <br>  <br> **Effect** The cavern mage uses their magical display to inspire another kobold within 30 feet. That kobold gains 4 temporary Hit Points that last until the start of the cavern mage's next turn. <br>  <br> > [!danger] Effect: Inspiring Display"
  - name: "Scamper"
    desc: "`pf2:1` **Requirements** The kobold cavern mage is adjacent to at least one enemy <br>  <br> **Effect** The kobold cavern mage Strides up to their Speed plus 5 feet and gains a +2 circumstance bonus to AC against reactions triggered by this movement. They must end this movement in a space that's not adjacent to any enemy."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Kobold cavern mages are born more than trained, hatching from eggs that absorbed particularly large amounts of primal earth energy. Although there are many elementals and even natural terrain features that can give rise to cavern mages, most are related to the cavern-dwelling earth nymphs known as lampads. These lonely and capricious fey are as enthusiastic to receive the company of a kobold tribe as the kobolds are for the protection they receive in return.

Kobolds are small reptilian humanoids. They lurk in dark spaces, usually tunnels and mines beneath the earth, in either warrens of their own design or complexes discovered and colonized after the original builders have moved on. Though kobolds are far more pragmatic than courageous, they use every inch of their cunning to even the playing field between themselves and other, stronger creatures. They attack from the darkness and at range, and kobold artificers and engineers master the art of simple but effective traps, which they use to protect their lairs. Kobolds are skilled at working together by necessity, and they often set up ambushes or hit-and-run assaults that allow them to do the most damage possible without being harmed in return.

Kobolds are diligent and hardworking creatures. While some kobolds live in communal collectives that maintain neutral relations with the creatures around them, they can be easily swayed into serving malevolent powers or megalomaniacal leaders. This is in part due to kobolds' innate pragmatism, as they would rather concede to servitude than risk being killed, but it is also in part due to a reverence for the power they generally lack. Notably, kobold eggs left in the proximity of magical creatures or places tend to absorb similar traits from the exposure. The resulting physical changes mark the appearance of each tribe, but a few lucky kobolds are also born with magical power that reflects their tribe's patron.

```statblock
creature: "Kobold Cavern Mage"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
