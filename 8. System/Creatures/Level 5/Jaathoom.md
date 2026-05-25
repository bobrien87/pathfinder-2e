---
type: creature
group: ["Air", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Jaathoom"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Air"
trait_02: "Elemental"
trait_03: "Genie"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]]"
languages: "Common, Sussuran ((Can't Speak Any Language); Cloud of Visions)"
skills:
  - name: Skills
    desc: "Acrobatics +14, Arcana +11, Athletics +11, Crafting +9, Deception +11, Diplomacy +13, Society +9, Stealth +12"
abilityMods: ["+4", "+5", "+2", "+2", "+2", "+4"]
abilities_top:
  - name: "Cloud of Visions"
    desc: "60 feet. <br>  <br> A jaathoom has [[Telepathy]] 60 feet but can only show images, not speak."
armorclass:
  - name: AC
    desc: "22; **Fort** +9, **Ref** +14, **Will** +11"
health:
  - name: HP
    desc: "55"
abilities_mid:
  - name: "Naturally Invisible"
    desc: "The jaathoom is [[Invisible]] at all times, though when they take a hostile action of any kind, they are [[Hidden]] instead of undetected until the start of their next turn, as the vague outline of their form is faintly visible for a short period of time."
  - name: "Turbulent Skies"
    desc: "20 feet. <br>  <br> All squares in the emanation are difficult terrain for Striding and Flying creatures. Creatures with the air trait are immune. <br>  <br> The jaathoom can activate or deactivate this aura as a single action with the concentrate trait."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scimitar +15 (`pf2:1`) (forceful, reach 10 ft., sweep), **Damage** 1d6+10 slashing"
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, finesse, magical, nonlethal, reach 10 ft., unarmed), **Damage** 1d4+10 bludgeoning"
  - name: "Ranged strike"
    desc: "Crashing Wind +16 (`pf2:1`) (air, arcane, range 20 ft.), **Damage** 1d8+8 bludgeoning"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 21, attack +13<br>**7th** [[Interplanar Teleport (to Astral Plane, Elemental Planes, or the Universe only)]]<br>**4th** [[Nightmare]], [[Vapor Form]]<br>**2nd** [[Illusory Creature]]<br>**1st** [[Detect Magic]], [[Ill Omen]], [[Illusory Object]], [[Sleep]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The jaathoom transforms into a Small or Medium air elemental or aerial animal, such as an owl. This doesn't affect their statistics, but it could change the damage type of their Strikes. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Hurricane Blast"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The jaathoom moves all creatures without the air trait in their turbulent skies aura 20 feet directly away, clockwise, or counterclockwise. A creature avoids being moved if it succeeds at a DC 21 [[Fortitude]] save."
  - name: "Ominous Dreams"
    desc: "`pf2:2` The jaathoom sends a prophetic dream to a sleeping creature within 10 feet. An unwilling creature avoids the vision if it succeeds at a DC 23 [[Will]] save. <br>  <br> The jaathoom chooses the dream's subject, but not its exact events. The target sees a brief vision of its future related to that subject, with the effect of [[Augury]]. If the result is bad or mixed, the creature is [[Frightened]] 2 and can't recover from being frightened until it wakes."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Possessing all the subtlety and elegance of air itself, the jaathooms of the Plane of Air operate within dreams, nightmares, and time.

Before mortal history, genies were some of the first creations of the cosmos to possess free will. Formed of elemental matter, they traversed the Universe and the six elemental planes of air, earth, fire, metal, water, and wood. The genies who remained on each elemental plane found their matter replaced with those elements. Genies of metal and wood appear in *Pathfinder Rage of Elements*.

Genie Shuyookhs
Older, wiser, and more powerful genies possess greater power and are revered with the title of shuyookh (typically adjusted to "sheikha" if the genie is female or "sheikh" for a male). Generally at least 5 levels higher than a typical example of their kind, a shuyookh gains additional spells. The basics of shuyookhs appear here in sidebars and are detailed further in *Rage of Elements*.

The most wondrous of their powers is their ability to grant wishes three times per year. This is not an innate ability but a ritual practice passed down over time in an attempt to replicate the wish-granting abilities of janns.

```statblock
creature: "Jaathoom"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
