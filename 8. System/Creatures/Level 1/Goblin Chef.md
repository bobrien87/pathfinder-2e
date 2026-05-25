---
type: creature
group: ["Goblin", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Goblin Chef"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Goblin"
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
    desc: "Nature +7, Society +4, Stealth +6, Survival +7, Cooking Lore +10"
abilityMods: ["+1", "+1", "+3", "+2", "+2", "+0"]
abilities_top:
  - name: "Good Enough to Eat"
    desc: "The goblin chef can turn otherwise inedible items into meals for others. They can provide food for any number of creatures without using the [[Subsist]] downtime activity as long as garbage is readily available. A non-goblin who eats the goblin chef's food must attempt a DC 14 [[Fortitude]] save. On a failure, they suffer an upset stomach for 1 day; if they attempt to willingly ingest anything else during that period, they must first succeed at a DC 4 flat check or the action is disrupted."
  - name: "Kitchen Specialist"
    desc: "For encounters involving cooking, a goblin chef is a 3rd-level challenge."
armorclass:
  - name: AC
    desc: "16; **Fort** +10, **Ref** +6, **Will** +5"
health:
  - name: HP
    desc: "24; **Immunities** sickened"
abilities_mid:
  - name: "+2 circumstance bonus against ingested poisons"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Cleaver +7 (`pf2:1`) (agile, backstabber, finesse), **Damage** 1d4+1 slashing"
  - name: "Melee strike"
    desc: "Jaws +7 (`pf2:1`) (finesse, unarmed), **Damage** 1d6+1 piercing"
spellcasting: []
abilities_bot:
  - name: "Eat a Pickle"
    desc: "`pf2:2` **Effect** The goblin chef draws a pickle and eats it or feeds it to an adjacent ally. The chef or ally gains 4 temporary Hit Points and ignores any penalties from emotion effects or fatigue for 1 round. <br>  <br> > [!danger] Effect: Eat a Pickle"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Goblins eat almost anything. Though they'll survive on raw or little-cooked meat, some prefer searing or frying their food first—or better yet, pickling it! A goblin chef can make anything edible (at least to a goblin).

Goblins can be found across Golarion, sometimes threatening taller humanoids (whom they refer to as "longshanks") and sometimes redeeming harmful history by working alongside others.

```statblock
creature: "Goblin Chef"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
