---
type: creature
group: ["Beast", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Minotaur Hunter"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]]"
languages: "Jotun, Common"
skills:
  - name: Skills
    desc: "Athletics +14, Intimidation +9, Survival +12"
abilityMods: ["+6", "+0", "+3", "-2", "+2", "-1"]
abilities_top:
  - name: "Perfect Orienteering"
    desc: "A minotaur automatically critically succeeds at Survival checks to Sense Direction or Track."
armorclass:
  - name: AC
    desc: "20; **Fort** +13, **Ref** +8, **Will** +10"
health:
  - name: HP
    desc: "70"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greataxe +14 (`pf2:1`) (reach 10 ft., sweep), **Damage** 1d12+8 slashing"
  - name: "Melee strike"
    desc: "Horn +14 (`pf2:1`) (unarmed), **Damage** 1d8+8 piercing"
spellcasting: []
abilities_bot:
  - name: "Axe Swipe"
    desc: "`pf2:2` The minotaur swings their axe in a wide arc, making greataxe Strikes against any two foes who are adjacent to each other and within the minotaur's reach. The multiple attack penalty does not increase until after both attacks are resolved."
  - name: "Hunted Fear"
    desc: "`pf2:1` The minotaur snorts and clomps as they hunt their prey, inspiring terror. The minotaur makes an Intimidation check to [[Demoralize]] all living creatures within 60 feet that can hear the minotaur but not see them. Roll once and apply the result to all creatures. <br>  <br> If the targets are in a maze or similarly difficult-to-navigate structure, the minotaur gains a +4 circumstance bonus to this check. Creatures that become frightened as a result also take a –2 circumstance penalty to Survival checks to avoid getting lost for 1 minute. Each target is temporarily immune for 1 minute. <br>  <br> > [!danger] Effect: Hunted Fear"
  - name: "Powerful Charge"
    desc: "`pf2:2` The minotaur Strides twice, then makes a horn Strike. If they moved at least 20 feet from their starting position, the Strike's damage is increased to 2d8+10."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A minotaur is a large humanoid with bovine features such as horns, hooves, and a layer of hair that covers their entire body. Their head also resembles that of a bull or cow, though with eyes that brim with curiosity or fury, depending on the minotaur's temperament. Though often mistaken for aggressive brutes due to their size and reputation, many minotaurs are skilled artisans who spend much of their lives perfecting their craft. Minotaur communities tend to be insular and are found at the heart of a cunning labyrinth or within a tangle of underground caverns.

The myth many minotaurs like to tell of their origin involves a stonemason living in ancient Iblydos. After accidentally insulting a hero-god, he was cursed to become the first minotaur. He then retreated into a series of caves beneath a temple he had built, but continued his work, sculpting stone statues for any who dared to brave the subterranean passages.

Sometimes, a lone minotaur is compelled, exiled, or chooses to live alone within a maze, a warren, or old ruins. This solitude drives them to become a monstrous tormentor who delights in hunting any who stumble across their lair. They slowly close in on their prey, thrilling in the terror of the hunted becoming lost within corridors the minotaur knows all too well. Only then does the minotaur charge in for the kill, cutting foes down with powerful strikes or impaling them on their sharp horns. Unfortunately, the world tends to judge all minotaurs by the stories of these lone, vicious hunters.

```statblock
creature: "Minotaur Hunter"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
