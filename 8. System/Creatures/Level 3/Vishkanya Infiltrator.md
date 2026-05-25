---
type: creature
group: ["Humanoid", "Vishkanya"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vishkanya Infiltrator"
level: "3"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Vishkanya"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Low-Light Vision]]"
languages: "Common, Vishkanyan"
skills:
  - name: Skills
    desc: "Acrobatics +9, Athletics +7, Deception +11, Diplomacy +9, Society +7, Stealth +11, Thievery +9"
abilityMods: ["+2", "+4", "+1", "+0", "+1", "+2"]
abilities_top:
  - name: "Flexible"
    desc: "The vishkanya is adept at dealing with tight situations. They have a +1 circumstance bonus to checks to [[Escape]]."
  - name: "Proficient Poisoner"
    desc: "The vishkanya doesn't lose the poison on a weapon due to a critically failed Strike."
  - name: "Sneak Attack"
    desc: "The vishkanya's Strikes deal an additional 1d6 precision damage to [[Off Guard]] creatures."
  - name: "Vishkanyan Venom"
    desc: "**Saving Throw** DC 20 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d4 poison damage (1 round) <br>  <br> **Stage 2** 1d4 poison damage and [[Off Guard]] (1 round) <br>  <br> **Stage 3** 1d4 poison damage, off-guard, and a –5-foot penalty to Speed (1 round)"
armorclass:
  - name: AC
    desc: "19; **Fort** +6, **Ref** +11, **Will** +8"
health:
  - name: HP
    desc: "45"
abilities_mid:
  - name: "+2 to Fortitude Saves vs. Poison"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Kukri +11 (`pf2:1`) (agile, finesse, trip), **Damage** 1d6+4 slashing"
  - name: "Melee strike"
    desc: "Shuriken +11 (`pf2:1`) (agile, thrown 20), **Damage** 1d4+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Envenom"
    desc: "`pf2:1` **Frequency** once per day <br>  <br> **Effect** Using either saliva or blood, the vishkanya applies vishkanyan venom to one weapon they're holding. To use their blood, they must be injured, or they can deal themself 1 slashing damage as part of the action."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These vishkanyas can meld with a crowd and slip into and out of places otherwise off-limits.

From a distance, vishkanyas share more than a passing resemblance to humans. However, a closer inspection reveals ophidian eyes with gold or white coloring, a forked tongue, and tiny, smooth scales set in serpentine patterns atop their skin. Even so, most onlookers assume these features to be an indicator of nephilim heritage or draconic magic, never suspecting how truly unusual the subject of their speculation is.

Among outsiders, little is known of the vishkanya ancestry other than that a vishkanya carries a potent venom within their blood and saliva, knowledge that has led to widespread fear and distrust. To avoid persecution, vishkanyas assimilate quietly into their chosen societies and maintain a culture of heavy subtlety. This clandestine life can draw vishkanyas to work that allows them to put their skills to good use, and they often take the roles of spy, mercenary, bodyguard, and even assassin. Some of the best-known guilds in the world employ vishkanyas, including the implacable Red Mantis Assassins and the famed Grand Sarret Conservatory for courtiers in the Impossible Kingdom of Jalmeray. In most cases, these employers know their employee's true identity, but not always.

Due to the measures they must take to ensure their survival, vishkanyas don't congregate openly. Instead, they meet in secret, creating support networks and advisory bodies. Leading these gatherings are the most respected of vishkanya women, who work diligently to keep their ancestry and traditions alive. These underground communities are slow to spread, and leaving them means abandoning what little social and cultural support a vishkanya has. As a result, very few vishkanyas have emigrated from their Vudran homelands into the Inner Sea region or other lands.

```statblock
creature: "Vishkanya Infiltrator"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
