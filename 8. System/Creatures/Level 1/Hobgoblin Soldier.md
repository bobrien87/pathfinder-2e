---
type: creature
group: ["Hobgoblin", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hobgoblin Soldier"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Hobgoblin"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Common, Goblin"
skills:
  - name: Skills
    desc: "Athletics +6, Stealth +6"
abilityMods: ["+3", "+3", "+2", "+0", "+2", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18 (20 with shield raised); **Fort** +5, **Ref** +6, **Will** +5"
health:
  - name: HP
    desc: "20"
abilities_mid:
  - name: "Formation"
    desc: "When it's adjacent to at least two other allies, the hobgoblin soldier gains a +1 circumstance bonus to AC and saving throws. This bonus increases to +2 to Reflex saves against area effects."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longsword +8 (`pf2:1`) (versatile p), **Damage** 1d8+3 slashing"
  - name: "Ranged strike"
    desc: "Shortbow +8 (`pf2:1`) (deadly d10, reload 0, range 60 ft.), **Damage** 1d6 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Soldiers make up the bulk of hobgoblin society, whether that society is a village or a military unit.

Hobgoblins may appear to outsiders to be the most civilized of goblinkind, but their civilization is hardly one of kindness and equality-instead, they revel in all that is militaristic, tyrannical, cruel, and destructive. Hobgoblins are singularly devoted to war, and their entire culture is built upon fostering and maintaining conflict while simultaneously proving their superiority in battle. Hobgoblins are highly organized, and they work efficiently and effectively in groups, whether that group is a small raiding party, a roving war band, or a fully regimented army. Hobgoblin rulers require little provocation before declaring war, and more often than not, such wars are waged to gain slaves or territory. Physically, hobgoblins stand about as tall as humans and have gray, ashen skin.

Hobgoblin society is organized along military lines, and every hobgoblin is effectively a member of the army. Each hobgoblin in a community has a rank in the military hierarchy, and individuals are naturally ambitious and obsessed with advancement. Hobgoblins are constantly expected to prove that they're fearless, ruthless, cunning, and strong. Demonstrating such aptitudes is an individual hobgoblin's best hope for promotion through the ranks, but failure leads only to cruel exploitation at the hands of their superiors. Though brutal, hobgoblin society is a true meritocracy, and all hobgoblins, regardless of age, gender, or birth, wield authority and earn respect from their peers based on their skill in battle. Even those individuals who serve in non-combat roles in hobgoblin society-blacksmiths, builders, cooks, messengers, quartermasters, and the like-know that they perform vital jobs that support the larger hobgoblin army, though they rarely rise above the rank of common soldier. Everyone contributes to the larger whole, ensuring that hobgoblin society is the strongest and most efficient it can be, and anyone who fails to do so is culled from the army and this hobgoblin society as dead weight. Hobgoblins don't usually engage in trade with other races, or even with other hobgoblin tribes, preferring to take what they want by force.

```statblock
creature: "Hobgoblin Soldier"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
