---
type: creature
group: ["Fey", "Gremlin"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mitflit"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Fey"
trait_02: "Gremlin"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+4; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +5, Diplomacy +1, Nature +3, Stealth +5, Thievery +5"
abilityMods: ["-1", "+3", "+0", "-1", "+1", "-1"]
abilities_top:
  - name: "Self-Loathing"
    desc: "A mitflit's self-loathing makes it easy to influence. It takes a -4 penalty to its Will DC against checks to [[Coerce]], [[Demoralize]], [[Make an Impression]], and [[Request]]."
  - name: "Vengeful Anger"
    desc: "As long as it isn't [[Frightened]], a mitflit gains a +2 status bonus to damage rolls against a creature that has previously damaged or tormented it."
armorclass:
  - name: AC
    desc: "14; **Fort** +2, **Ref** +7, **Will** +4"
health:
  - name: HP
    desc: "10; **Weaknesses** cold iron 2"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +8 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6-1 piercing"
  - name: "Melee strike"
    desc: "Dart +8 (`pf2:1`) (agile, thrown 20), **Damage** 1d4-1 piercing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 16, attack +8<br>**2nd** [[Speak with Animals (Arthropods Only, At Will)]]<br>**1st** [[Bane]], [[Prestidigitation]]"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Mitflits are self-loathing and pitiful cowards, easily bullied into servitude by other creatures or even slightly more powerful mitflit leaders. They tame insects, spiders, and other small vermin to serve as faithful allies. Mitflits have lost most of their ancestral magic, leaving them to feel incomplete and full of doubt and insecurity. Mitflits find companionship in the other base creatures of the world, and forge strong bonds of friendship with vermin, the only other beings that seem willing to accept them. A social structure, even one in which they are bullied, partially fills the hole within most mitflits' personalities, and they rarely rebel or last out unless their rage hits a breaking point.

Gremlins are cruel fey tricksters and saboteurs who have fully acclimated to life in the Universe, finding distinct niches for their inventive destructiveness. Nearly all gremlins delight in ruining or breaking things, whether it's something physical like a device or vehicle or something intangible such as an alliance or relationship. A gremlin's greatest joy is watching the collapse of complex creations, preferably after the slightest, carefully targeted nudge from the gremlin. Gremlins tend to denigrate, bully, or even slaughter their lesser kin, particularly mitflits, whom stronger gremlins derisively call "baggies."

```statblock
creature: "Mitflit"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
