---
type: creature
group: ["Elemental", "Genie"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Faydhaan"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Elemental"
trait_02: "Genie"
trait_03: "Water"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]], [[Wavesense]] (imprecise) 60 feet"
languages: "Common, Thalassic, Muan, Petran, Pyric, Sussuran, Talican (Truespeech)"
skills:
  - name: Skills
    desc: "Athletics +19, Crafting +16, Deception +18, Diplomacy +20, Nature +18, Performance +20, Society +16, Stealth +18"
abilityMods: ["+4", "+5", "+2", "+1", "+3", "+5"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "28; **Fort** +17, **Ref** +18, **Will** +18"
health:
  - name: HP
    desc: "145; **Resistances** fire 10"
abilities_mid:
  - name: "Turbulent Seas"
    desc: "40 feet. <br>  <br> Water in the aura that is also in the same body of water as the faydhaan is difficult terrain for Swimming creatures. Creatures with the water trait are immune."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Trident +20 (`pf2:1`) (magical, reach 10 ft.), **Damage** 2d8+10 piercing"
  - name: "Melee strike"
    desc: "Fist +20 (`pf2:1`) (agile, magical, nonlethal, reach 10 ft., unarmed), **Damage** 1d4+10 bludgeoning"
  - name: "Melee strike"
    desc: "Trident +21 (`pf2:1`) (magical, thrown 20), **Damage** 2d8+10 piercing"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 24, attack +12<br>**7th** [[Interplanar Teleport (to Astral Plane, Elemental Planes, or the Universe only)]]<br>**5th** [[Control Water]] (At Will), [[Truespeech]] (At Will), [[Truespeech]] (Constant)<br>**4th** [[Hydraulic Torrent]]<br>**2nd** [[Invisibility]], [[Water Breathing]]<br>**1st** [[Create Water]] (At Will), [[Detect Magic]], [[Hydraulic Push]] (At Will)"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The faydhaan transforms into a Small or Medium water elemental, aquatic animal, or humanoid. This doesn't affect their statistics, but it could change the damage type of their Strikes. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Gift of Hospitality"
    desc: "`pf2:3` The faydhaan gives another willing creature a magical gift or an agreeable conversation. The creature gains a +2 status bonus to Society and Diplomacy checks. A creature can't have more than one gift at a time, and a faydhaan can't grant more than one gift at a time. <br>  <br> The gift ends if the target acts hostile, or if the faydhaan renounces the recipient (a single action). <br>  <br> > [!danger] Effect: Gift of Hospitality"
  - name: "Skewer"
    desc: "`pf2:1` The faydhaan makes a trident Strike, dealing an extra 2d6 persistent bleed damage on a hit (4d6 on a critical hit)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The faydhaans of the Plane of Water are more powerful than the other genies dwelling on the elemental planes, but they prefer to forge alliances through diplomacy and flattery.

Before mortal history, genies were some of the first creations of the cosmos to possess free will. Formed of elemental matter, they traversed the Universe and the six elemental planes of air, earth, fire, metal, water, and wood. The genies who remained on each elemental plane found their matter replaced with those elements. Genies of metal and wood appear in *Pathfinder Rage of Elements*.

Genie Shuyookhs
Older, wiser, and more powerful genies possess greater power and are revered with the title of shuyookh (typically adjusted to "sheikha" if the genie is female or "sheikh" for a male). Generally at least 5 levels higher than a typical example of their kind, a shuyookh gains additional spells. The basics of shuyookhs appear here in sidebars and are detailed further in *Rage of Elements*.

The most wondrous of their powers is their ability to grant wishes three times per year. This is not an innate ability but a ritual practice passed down over time in an attempt to replicate the wish-granting abilities of janns.

```statblock
creature: "Faydhaan"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
