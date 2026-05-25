---
type: creature
group: ["Aberration", "Void"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sceaduinar"
level: "7"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: "Void"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Greater Darkvision]], [[Lifesense]] (precise) 120 feet"
languages: "Aklo"
skills:
  - name: Skills
    desc: "Acrobatics +17, Athletics +13, Intimidation +13, Occultism +15, Stealth +17"
abilityMods: ["+2", "+6", "+4", "+2", "+4", "+0"]
abilities_top:
  - name: "Drain Life"
    desc: "When the sceaduinar damages a living creature with its jaws Strike, the sceaduinar gains 5 temporary Hit Points and the creature must succeed at a DC 25 [[Fortitude]] save or become [[Drained]] 1. <br>  <br> Further damage dealt to the creature by the sceaduinar increases the drained value by 1 on a failed save, to a maximum of drained 4. <br>  <br> > [!danger] Effect: Drain Life"
  - name: "Entropic Touch"
    desc: "Void damage dealt by a sceaduinar damages undead and creatures with void healing as if it were vitality damage. The sceaduinar's melee Strikes have the benefits of the *[[Ghost Touch]]* property rune on attacks against incorporeal undead."
armorclass:
  - name: AC
    desc: "25; **Fort** +16, **Ref** +18, **Will** +14"
health:
  - name: HP
    desc: "100; void healing; **Immunities** death effects, drained; **Weaknesses** holy 10; **Resistances** physical 5 except adamantine"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Void Child"
    desc: "Sceaduinar have neither souls nor the ability to create. A sceaduinar is immune to effects that target a soul (such as [[Seize Soul]] or a [[Resurrect]] ritual) or that require knowledge of a creature's identity (such as [[Scrying]]), and critically fails Crafting checks."
  - name: "Wing Flash"
    desc: "`pf2:r` **Trigger** A creature attempts a melee attack against a sceaduinar or an Acrobatics check to [[Tumble Through]] the sceaduinar's space <br>  <br> **Effect** The sceaduinar flexes its wings to emit a brief pulse of void energy that deals 4d6 void damage to the triggering creature (DC 22 [[Reflex]] save)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +18 (`pf2:1`) (agile, finesse, magical, unarmed), **Damage** 2d6+4 piercing plus 2d6 void plus [[Drain Life]]"
  - name: "Melee strike"
    desc: "Wing +18 (`pf2:1`) (agile, finesse, magical, reach 10 ft.), **Damage** 2d6+4 slashing plus 2d6 void"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 25, attack +0<br>**4th** [[Translocate]]<br>**2nd** [[Darkness]], [[Dispel Magic]], [[Silence]]<br>**1st** [[Grim Tendrils]], [[Harm]], [[Harm]], [[Void Warp]]"
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Strange creatures born from jagged crystals in the heart of the Void, sceaduinar are fueled by its void energy and driven to extinguish all life. Resembling crystalline gargoyles with serrated limbs and sharp, bat-like faces, sceaduinar stand about 7 feet tall and weigh around 100 pounds.

These malevolent beings sometimes gather in great packs of their own kind. Despite their intelligence, they act like cunning, feral beasts for the most part, though they occasionally build tools to aid them in extinguishing life. Sceaduinar sail through the great voids of their home plane, seeking to destroy any sparks of life that find their way into that deadly realm-even the twisted sparks found in undead creatures.

When they discover portals to other planes, sceaduinar swarm through in great numbers, slaughtering all they come across. While dwelling outside the Void is uncomfortable for sceaduinar, they can exist for extended periods of time apart from their home. Of course, the feeling of a plane where void energy isn't the rule doesn't improve these creatures' attitude, and as a result, they tend to be particularly cruel and violent when encountered in such realms.

```statblock
creature: "Sceaduinar"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
