---
type: creature
group: ["Elemental", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ifrit"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Elemental"
trait_02: "Fire"
trait_03: "Genie"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Darkvision]]"
languages: "Common, Pyric (Truespeech)"
skills:
  - name: Skills
    desc: "Arcana +14, Athletics +22, Crafting +14, Deception +19, Diplomacy +17, Intimidation +19, Society +14"
abilityMods: ["+5", "+3", "+4", "+1", "+2", "+4"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Burning Grasp"
    desc: "When the ifrit [[Grab|Grabs]] or [[Restrains]] a creature, that creature takes 2d6 fire damage, and takes 2d6 fire damage at the end of each of its turns until freed."
armorclass:
  - name: AC
    desc: "28; **Fort** +18, **Ref** +17, **Will** +20"
health:
  - name: HP
    desc: "175; **Immunities** fire; **Weaknesses** cold 10, water 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scimitar +21 (`pf2:1`) (fire, forceful, magical, reach 10 ft., sweep), **Damage** 2d6+11 slashing plus 2d6 fire"
  - name: "Melee strike"
    desc: "Fist +20 (`pf2:1`) (agile, magical, reach 10 ft., unarmed), **Damage** 1d4+11 bludgeoning plus 2d6 fire"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 29, attack +19<br>**7th** [[Interplanar Teleport (to Astral Plane, Elemental Planes, or the Universe only)]]<br>**5th** [[Truespeech]] (Constant)<br>**3rd** [[Fireball]]<br>**2nd** [[Invisibility]]<br>**1st** [[Detect Magic]], [[Ignition]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The ifrit transforms into a Small or Medium fire elemental or reptile, such as a snake. This doesn't affect their statistics but could change the damage type of their Strikes. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Combat Grab"
    desc: "`pf2:1` **Requirements** The ifrit has a hand free <br>  <br> **Effect** The ifrit makes a melee Strike. If the Strike hits, the target is [[Grabbed]] in the ifrit's free hand."
  - name: "Wings of Flame"
    desc: "`pf2:1` The ifrit grows flaming wings from their back. They gain a fly Speed of 35 feet for 1 minute. The flames also create an aura in a 5-foot emanation around the ifrit. <br>  <br> Any creature that ends its turn in the aura takes @Damage[2d6[fire]|options:area-damage] damage with a DC 25 [[Reflex]] save."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The fierce and unforgiving ifrits hail from the Plane of Fire, where they build metropolises and trade centers that draw extraplanar travelers. Many ifrits are tyrannical or warmongering, and most use their might to accomplish their goals.

Before mortal history, genies were some of the first creations of the cosmos to possess free will. Formed of elemental matter, they traversed the Universe and the six elemental planes of air, earth, fire, metal, water, and wood. The genies who remained on each elemental plane found their matter replaced with those elements. Genies of metal and wood appear in *Pathfinder Rage of Elements*.

Genie Shuyookhs
Older, wiser, and more powerful genies possess greater power and are revered with the title of shuyookh (typically adjusted to "sheikha" if the genie is female or "sheikh" for a male). Generally at least 5 levels higher than a typical example of their kind, a shuyookh gains additional spells. The basics of shuyookhs appear here in sidebars and are detailed further in *Rage of Elements*.

The most wondrous of their powers is their ability to grant wishes three times per year. This is not an innate ability but a ritual practice passed down over time in an attempt to replicate the wish-granting abilities of janns.

```statblock
creature: "Ifrit"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
