---
type: creature
group: ["Air", "Earth"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Jann"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Air"
trait_02: "Earth"
trait_03: "Elemental"
trait_04: "Fire"
trait_05: "Genie"
trait_06: "Metal"
trait_07: "Water"
perception:
  - name: Perception
    desc: "+11; [[Darkvision]]"
languages: "Common, Muan, Petran, Pyric, Sussuran, Talican, Thalassic (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +8, Arcana +10, Crafting +8, Deception +7, Survival +11"
abilityMods: ["+4", "+2", "+2", "+3", "+3", "+1"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "20; **Fort** +10, **Ref** +10, **Will** +13"
health:
  - name: HP
    desc: "60; **Resistances** fire 5, electricity 5, cold 5, air 5, earth 5, metal 5, wood 5, water 5"
abilities_mid:
  - name: "Commanding Presence"
    desc: "20 feet. <br>  <br> A creature that enters the aura must succeed at a DC 19 [[Will]] save or be [[Frightened]] 1 ([[Frightened]] 2 on a critical failure) and is then temporarily immune for 1 minute. <br>  <br> A genie (with the exception of another jann) takes a –4 circumstance penalty to its save."
  - name: "Elemental Resistance"
    desc: "The jann's elemental resistance applies to cold, electricity, and fire damage, as well as all damage from elemental sources (including environmental damage from the elemental planes and damage from anything with the air, earth, fire, metal, water, or wood trait)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scimitar +14 (`pf2:1`) (forceful, sweep), **Damage** 1d6+7 slashing plus [[All Made One]]"
  - name: "Melee strike"
    desc: "Fist +14 (`pf2:1`) (agile, magical, nonlethal, unarmed), **Damage** 1d4+7 bludgeoning plus [[All Made One]]"
  - name: "Ranged strike"
    desc: "Composite Shortbow +12 (`pf2:1`) (deadly d10, propulsive, reload 0, range 60 ft.), **Damage** 1d6+5 piercing plus [[All Made One]]"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 21, attack +13<br>**7th** [[Interplanar Teleport (to Astral Plane, Elemental Planes, or the Universe only)]]<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Read Omens]]<br>**2nd** [[Invisibility]]<br>**1st** [[Detect Magic]], [[Know the Way]]"
abilities_bot:
  - name: "All Made One"
    desc: "`pf2:1` The jann calls upon all of the elements that make up their being to gain an additional arcane spell they can cast at will and empower their Strikes with the element, dealing an extra 1d4 damage of the listed type. These benefits last until the jann uses this ability again. <br>  <br> - Air [[Tailwind]], 1d4 electricity;  <br>  <br> - Earth [[Pummeling Rubble]], 1d4 bludgeoning;  <br>  <br> - Fire [[Breathe Fire]], 1d4 fire;  <br>  <br> - Metal [[Thunderstrike]], 1d4 electricity;  <br>  <br> - Water [[Hydraulic Push]], 1d4 bludgeoning;  <br>  <br> - Wood [[Summon Plant or Fungus]], 1d4 piercing."
  - name: "Change Shape"
    desc: "`pf2:1` The jann transforms into any Small or Medium animal. This doesn't affect their statistics, but it could change the damage type of their Strikes. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Wanderer's Wish"
    desc: "`pf2:3` **Frequency** three times per year <br>  <br> **Effect** The jann instantly grants the benefits of a critical success with the [[Wish]] ritual to a mortal creature. This has no cost. That creature specifies what they wish for, but the interpretation is up to the jann. A jann typically attempts to grant wishes in a way that encourages growth and exploration. <br>  <br> A summoned jann can't use this ability."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

All six elements build each jann and fill them with a constant desire to travel, typically jaunting about the Universe. The eldest among geniekind, they command respect from their distant offspring. Any jann can grant wishes, not just shuyookhs—a vestige of their ancient power.

Before mortal history, genies were some of the first creations of the cosmos to possess free will. Formed of elemental matter, they traversed the Universe and the six elemental planes of air, earth, fire, metal, water, and wood. The genies who remained on each elemental plane found their matter replaced with those elements. Genies of metal and wood appear in *Pathfinder Rage of Elements*.

Genie Shuyookhs
Older, wiser, and more powerful genies possess greater power and are revered with the title of shuyookh (typically adjusted to "sheikha" if the genie is female or "sheikh" for a male). Generally at least 5 levels higher than a typical example of their kind, a shuyookh gains additional spells. The basics of shuyookhs appear here in sidebars and are detailed further in *Rage of Elements*.

The most wondrous of their powers is their ability to grant wishes three times per year. This is not an innate ability but a ritual practice passed down over time in an attempt to replicate the wish-granting abilities of janns.

```statblock
creature: "Jann"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
