---
type: creature
group: ["Fiend", "Swarm"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vescavor Swarm"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Fiend"
trait_02: "Swarm"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Darkvision]]"
languages: "Chthonian"
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +10, Stealth +13"
abilityMods: ["-2", "+5", "+4", "-3", "+1", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "21; **Fort** +11, **Ref** +15, **Will** +9"
health:
  - name: HP
    desc: "60; **Immunities** mental, precision; **Weaknesses** area damage 5, cold iron 5, holy 5, splash damage 5; **Resistances** bludgeoning 5, piercing 5, slashing 2"
abilities_mid:
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Devour All"
    desc: "`pf2:2` The swarm eat away the very earth beneath their feet. The swarms Strides. All squares they occupy during their movement becomes difficult terrain. Any creatures they move through must succeed a DC 21 [[Reflex]] save or fall [[Prone]]."
  - name: "Maddening Gibbers"
    desc: "`pf2:2` Each stupefied creature in the swarm's space must attempt a DC 21 [[Will]] save saving throw as the swarm yammers the endless chorus of the Outer Rifts. <br> - **Critical Success** The target is unaffected and is temporarily immune to Maddening Gibbers for 1 minute. <br> - **Success** The target is unaffected and is immune to Maddening Gibbers for 1 round. <br> - **Failure** The target becomes [[Confused]] for 1 round. <br> - **Critical Failure** The target becomes confused for 1 round and can't target fiends while confused in this way."
  - name: "Ravenous Bites"
    desc: "`pf2:1` Each enemy in the swarm's space takes 3d6 piercing damage (DC 20 [[Fortitude]] save). A creature that fails its save is also [[Stupefied 1]] for 1 round."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The most common and numerous vescavors are the raving swarms. If left alone and unchecked, many believe they would eventually consume themselves once everything else in the immediate vicinity was consumed. What is even more vexing than their hunger is their song. While it sounds like gibberish at first, once bitten, the song will drive people into chaos.

These gluttonous green vermin travel from the Outer Rifts in an endless search for food. Along the way, these acrid wasps devour everything in sight. Not even the ground itself is spared from their appetite. While any single vescavor is no problem, they travel in swarms to overwhelm anything trying to stop them. In a truly unfortunate situation, several swarms will be gathered and led by a vescavor queen. These queens, while fearsome on their own, can drive their brood into a feeding rage unlike any other. Swarms found without a queen are directionless, destroying anything around them indiscriminately.

Whenever a vescavor swarm is not eating, it gibbers mind-numbing songs from the fiends' dark world. Adapted to the shrieking jungles of their home plane, they issue a call that confuses and corrupts mortals.

Philosophers who ponder the Outer Rifts often conjecture as to what kind of soul forms a vescavor. The idea of insect souls being sent to the Outer Rifts is often laughed off but never entirely dismissed. Some assume that they are demons of gluttony, plain and simple. Some of the more creative explanations of vescavor origins posit that all the bits of soul eaten up by attacking demons are what coalesce into these endless swarms. Such an explanation would account for how these endlessly feeding demons also seem to be endless in number.

```statblock
creature: "Vescavor Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
