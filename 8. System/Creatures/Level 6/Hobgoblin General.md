---
type: creature
group: ["Hobgoblin", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hobgoblin General"
level: "6"
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
    desc: "+13; [[Darkvision]]"
languages: "Common, Goblin"
skills:
  - name: Skills
    desc: "Acrobatics +12, Athletics +15, Intimidation +14, Stealth +12"
abilityMods: ["+4", "+3", "+2", "+0", "+1", "+2"]
abilities_top:
  - name: "General's Cry"
    desc: "When a hobgoblin general rolls initiative, as long as they can perceive at least one foe, they can yell a mighty battle cry. The hobgoblin general attempts an Intimidate check to `act demoralize` a single foe within 60 feet as a free action. If successful, any ally can, as its first action on its first turn of the combat, Stride up to double its speed as a single action."
  - name: "Polearm Critical Specialization"
    desc: "On a critical hit, the target of the critical hit is moved 5 feet in a direction of the hobgoblin general's choice."
armorclass:
  - name: AC
    desc: "25; **Fort** +12, **Ref** +15, **Will** +13"
health:
  - name: HP
    desc: "90"
abilities_mid:
  - name: "Formation"
    desc: "When it's adjacent to at least two other allies, the hobgoblin general gains a +1 circumstance bonus to AC and saving throws. This bonus increases to +2 to Reflex saves against area effects."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Glaive +17 (`pf2:1`) (deadly d8, forceful, reach 10 ft.), **Damage** 1d8+10 slashing"
  - name: "Ranged strike"
    desc: "Composite Shortbow +15 (`pf2:1`) (brutal, deadly d10, propulsive, reload 0, range 60 ft.), **Damage** 1d6+8 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Hobgoblin generals serve as leaders of entire armies and rulers of hobgoblin settlements. A general does not permit the luxuries of rule to soften them. They lead their forces on the field of battle and view this opportunity to excel in a fight at the head of an army as the true reward for a life spent honing one's skills in battle.

Hobgoblins may appear to outsiders to be the most civilized of goblinkind, but their civilization is hardly one of kindness and equality-instead, they revel in all that is militaristic, tyrannical, cruel, and destructive. Hobgoblins are singularly devoted to war, and their entire culture is built upon fostering and maintaining conflict while simultaneously proving their superiority in battle. Hobgoblins are highly organized, and they work efficiently and effectively in groups, whether that group is a small raiding party, a roving war band, or a fully regimented army. Hobgoblin rulers require little provocation before declaring war, and more often than not, such wars are waged to gain slaves or territory. Physically, hobgoblins stand about as tall as humans and have gray, ashen skin.

Hobgoblin society is organized along military lines, and every hobgoblin is effectively a member of the army. Each hobgoblin in a community has a rank in the military hierarchy, and individuals are naturally ambitious and obsessed with advancement. Hobgoblins are constantly expected to prove that they're fearless, ruthless, cunning, and strong. Demonstrating such aptitudes is an individual hobgoblin's best hope for promotion through the ranks, but failure leads only to cruel exploitation at the hands of their superiors. Though brutal, hobgoblin society is a true meritocracy, and all hobgoblins, regardless of age, gender, or birth, wield authority and earn respect from their peers based on their skill in battle. Even those individuals who serve in non-combat roles in hobgoblin society-blacksmiths, builders, cooks, messengers, quartermasters, and the like-know that they perform vital jobs that support the larger hobgoblin army, though they rarely rise above the rank of common soldier. Everyone contributes to the larger whole, ensuring that hobgoblin society is the strongest and most efficient it can be, and anyone who fails to do so is culled from the army and this hobgoblin society as dead weight. Hobgoblins don't usually engage in trade with other races, or even with other hobgoblin tribes, preferring to take what they want by force.

```statblock
creature: "Hobgoblin General"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
