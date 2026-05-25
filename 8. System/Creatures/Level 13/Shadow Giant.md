---
type: creature
group: ["Giant", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Shadow Giant"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Shadow"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Darkvision]]"
languages: "Common, Jotun, Shadowtongue"
skills:
  - name: Skills
    desc: "Athletics +27, Intimidation +24, Stealth +21"
abilityMods: ["+8", "+2", "+5", "+0", "+1", "+3"]
abilities_top:
  - name: "Pall of Shadow"
    desc: "When a shadow giant hits with a melee attack, the target must succeed at a DC 30 [[Fortitude]] save or become [[Drained]] 1 and take a –1 status penalty to Perception checks involving sight as long as they remain drained. On a critical failure, this condition doesn't heal naturally and can be removed only with magic."
armorclass:
  - name: AC
    desc: "33; **Fort** +25, **Ref** +20, **Will** +23"
health:
  - name: HP
    desc: "275"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Spiked Chain +27 (`pf2:1`) (disarm, reach 10 ft., trip), **Damage** 3d8+18 slashing plus [[Pall Of Shadow]]"
  - name: "Melee strike"
    desc: "Fist +26 (`pf2:1`) (agile, nonlethal, reach 10 ft., unarmed), **Damage** 3d8+18 bludgeoning plus [[Pall Of Shadow]]"
spellcasting: []
abilities_bot:
  - name: "Shadow Chain"
    desc: "`pf2:2` Shadows extend the giant's chain as they make a spiked chain Strike, increasing their reach to 60 feet for that Strike. If this hits, the target must succeed at a DC 33 [[Will]] save or be teleported to an empty space within the shadow giant's normal reach."
  - name: "Shadowcloak"
    desc: "`pf2:1` The shadow giant gains the effect of the [[Blur]] spell for 1 minute or until it is exposed to direct sunlight, whichever comes first."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Shadow giants are natives of the Netherworld, where they have dwelled in perpetual twilight for millennia. They live in familiar groups and uphold a nomadic way of life as they roam across ancestral lands between shadowy forests and misty chasms. These hunter-gatherers pass down lore through oral histories, conduct pilgrimages to unholy ziggurats of black stone, and bathe in the blood of their long-standing foes, including rival shadow giant clans and fiends of the Netherworld intent on enslaving their kind.

Standing 15 feet tall, with gray skin and hair only a shade lighter, shadow giants are fearsome foes with a well-earned reputation as zealous warmongers and ruthless combatants. They rarely interact with outsiders, though they may treat with proven warriors who show the giants the respect and deference they feel they deserve.

Giants are massive humanoid creatures who live in remote regions throughout the world. They vary widely but are united in their hunger, requiring sustenance of their own element along with the feasts one would expect from such a massive humanoid. Although a simple matter for some giants, more esoteric types find this need a harsh reality. While a massive fistful of ice or snow alongside their meal will satisfy a frost giant, shadow giants hunger for the coagulated shadows of the Netherworld.

```statblock
creature: "Shadow Giant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
