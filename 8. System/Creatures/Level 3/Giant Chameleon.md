---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Chameleon"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +9, Stealth +10"
abilityMods: ["+5", "+3", "+1", "-4", "+3", "-2"]
abilities_top:
  - name: "Camouflage"
    desc: "The giant chameleon can change its coloration to match its surroundings. It doesn't need cover to attempt to [[Hide]] with a Stealth check."
  - name: "Tongue Grab"
    desc: "If the giant chameleon hits a creature with a tongue Strike, that creature becomes [[Grabbed]] by the giant chameleon. The target isn't [[Immobilized]], but it can't move beyond the reach of the giant chameleon's tongue. A creature can sever the tongue with an attack that hits AC 15 and deals at least 4 slashing damage. Though this doesn't deal any damage to the giant chameleon, it prevents it from using its tongue Strike until it regrows its tongue, which takes a week."
armorclass:
  - name: AC
    desc: "18 all-around vision; **Fort** +8, **Ref** +12, **Will** +8"
health:
  - name: HP
    desc: "60"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +12 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 1d10+7 piercing"
  - name: "Melee strike"
    desc: "Tongue +12 (`pf2:1`) (agile, reach 15 ft.), **Damage**  plus [[Tongue Grab]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Giant chameleons are legendary for their ability to change their skin color in response to their surroundings. Their eyes are capable of peering in different directions independently, making them almost as difficult to sneak up on as they are to notice in the first place.

```statblock
creature: "Giant Chameleon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
