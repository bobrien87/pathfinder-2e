---
type: creature
group: ["Hobgoblin", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hobgoblin Archer"
level: "4"
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
    desc: "+10; [[Darkvision]]"
languages: "Common, Goblin"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +8, Stealth +10"
abilityMods: ["+2", "+4", "+2", "+0", "+2", "-1"]
abilities_top:
  - name: "Crossbow Precision"
    desc: "The first time the archer hits with a crossbow attack in a round, it deals 1d8 extra precision damage."
  - name: "Perfect Aim"
    desc: "The hobgoblin archer ignores the [[Concealed]] condition. <br>  <br> Their targets don't benefit from lesser cover, and they reduce the AC bonus from standard cover by 2 against the hobgoblin archer's attack."
armorclass:
  - name: AC
    desc: "23; **Fort** +10, **Ref** +12, **Will** +8"
health:
  - name: HP
    desc: "50"
abilities_mid:
  - name: "Formation"
    desc: "When it's adjacent to at least two other allies, the hobgoblin archer gains a +1 circumstance bonus to AC and saving throws. This bonus increases to +2 to Reflex saves against area effects."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +12 (`pf2:1`) (agile, versatile s), **Damage** 1d6+4 piercing"
  - name: "Ranged strike"
    desc: "Crossbow +14 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+2 piercing plus [[Crossbow Precision]]"
spellcasting: []
abilities_bot:
  - name: "Running Reload"
    desc: "`pf2:1` The archer Strides, Steps, or [[Sneaks]], then Interacts to reload."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Bands of hobgoblin soldiers typically have at least one archer among their ranks. In smaller groups, the hobgoblin archer also serves as that band's captain.

Hobgoblins may appear to outsiders to be the most civilized of goblinkind, but their civilization is hardly one of kindness and equality-instead, they revel in all that is militaristic, tyrannical, cruel, and destructive. Hobgoblins are singularly devoted to war, and their entire culture is built upon fostering and maintaining conflict while simultaneously proving their superiority in battle. Hobgoblins are highly organized, and they work efficiently and effectively in groups, whether that group is a small raiding party, a roving war band, or a fully regimented army. Hobgoblin rulers require little provocation before declaring war, and more often than not, such wars are waged to gain slaves or territory. Physically, hobgoblins stand about as tall as humans and have gray, ashen skin.

Hobgoblin society is organized along military lines, and every hobgoblin is effectively a member of the army. Each hobgoblin in a community has a rank in the military hierarchy, and individuals are naturally ambitious and obsessed with advancement. Hobgoblins are constantly expected to prove that they're fearless, ruthless, cunning, and strong. Demonstrating such aptitudes is an individual hobgoblin's best hope for promotion through the ranks, but failure leads only to cruel exploitation at the hands of their superiors. Though brutal, hobgoblin society is a true meritocracy, and all hobgoblins, regardless of age, gender, or birth, wield authority and earn respect from their peers based on their skill in battle. Even those individuals who serve in non-combat roles in hobgoblin society-blacksmiths, builders, cooks, messengers, quartermasters, and the like-know that they perform vital jobs that support the larger hobgoblin army, though they rarely rise above the rank of common soldier. Everyone contributes to the larger whole, ensuring that hobgoblin society is the strongest and most efficient it can be, and anyone who fails to do so is culled from the army and this hobgoblin society as dead weight. Hobgoblins don't usually engage in trade with other races, or even with other hobgoblin tribes, preferring to take what they want by force.

```statblock
creature: "Hobgoblin Archer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
