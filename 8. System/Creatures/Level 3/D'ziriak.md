---
type: creature
group: ["Aberration", "Shadow"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "D'ziriak"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: "Shadow"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Dziriak, Shadowtongue (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Arcana +8, Athletics +6, Occultism +10, Stealth +10, Survival +8"
abilityMods: ["+1", "+3", "+1", "+1", "+3", "+4"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "18; **Fort** +6, **Ref** +12, **Will** +10"
health:
  - name: HP
    desc: "45"
abilities_mid:
  - name: "Glow"
    desc: "20 feet. The colorful runes that decorate a d'ziriak's body create dim light. The natural bioluminescence is specially adapted to the Netherworld, able to overcome magical darkness as if it were magical light with a rank equal to half the d'ziriak's level rounded up."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +12 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d10+4 piercing"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 19, attack +9<br>**7th** [[Interplanar Teleport (Self only, to Netherworld only)]]"
abilities_bot:
  - name: "Dazzling Burst"
    desc: "`pf2:2` Dazzling Burst `pf2:2` (light, visual) The d'ziriak causes their body to flare with intense colorful light. Non-d'ziriaks in a @Template[type:emanation|distance:20] must attempt a DC 20 [[Fortitude]] save. After using this ability, the d'ziriak loses their glow for 24 hours; during this time they can't use Dazzling Burst again. A creature that attempts this save is immune to all Dazzling Bursts for 1 minute. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Dazzled]] for 1 round. <br> - **Failure** The creature is dazzled for 1 minute. <br> - **Critical Failure** The creature is [[Blinded]] for 1 round and dazzled for 1 minute."
  - name: "Double Claw"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The d'ziriak makes two claw Strikes. If both hit the same creature, combine their damage for the purpose of resistances and weaknesses. This counts as two attacks for the d'ziriak's multiple attack penalty, and the penalty doesn't increase until after both attacks."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These strange creatures are native to the Netherworld, where their colorful nature is in opposition to that realm's overwhelmingly monochromatic palette. Averaging 7 feet in height, d'ziriaks have four arms, two legs, and a termite-like abdomen. The larger pair of arms, used for most tasks, have five-fingered hands with sharp, insectile claws. The smaller pair of arms are reserved for fine manipulations and are not effective in combat.

D'ziriaks' otherwise-dull brown carapaces are decorated with numerous runes glowing in bright colors. These tattoo-like runes indicate an individual's role in d'ziriak society and set them apart from their home plane's other native inhabitants. The runes glow with natural bioluminescence, and d'ziriaks can make them flare brightly for an instant, at the expense of overstressing the biochemical glands that create and maintain the runes for an extended time. The color and shape of the runes are partially natural but can be carefully customized over time to fit the individual's station.

The D'ziriak language is a mix of buzzes and chitters and is spoken by few other creatures. D'ziriaks prefer to communicate with other species using telepathy rather than endure the sound of their language being "butchered by fleshy throats." D'ziriaks organize into hive cities led by a king and queen. These hive cities consist of impressive spires, yet the towers are only the foremost part of the settlement, with many chambers reaching deep below, used as residences, workshops, and fungus farms. D'ziriak settlements are lit inside and out with alchemical and magical light sources, often in the shape of runes. These dimly glowing towers provide travelers with landmarks and perhaps promise safe havens on the otherwise gloomy Netherworld.

```statblock
creature: "D'ziriak"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
