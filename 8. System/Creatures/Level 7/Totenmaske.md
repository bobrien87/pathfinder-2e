---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Totenmaske"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]]"
languages: "Common, Necril"
skills:
  - name: Skills
    desc: "Acrobatics +15, Deception +17, Stealth +17, Thievery +15"
abilityMods: ["+4", "+6", "+2", "+1", "+2", "+3"]
abilities_top:
  - name: "Shape Flesh"
    desc: "After spending 1 minute in contact with a [[Paralyzed]], [[Unconscious]], or willing creature, a totenmaske can reshape the target's face, causing flesh to cover vital features. The target can attempt a DC 25 [[Fortitude]] save to resist; a critical success grants temporary immunity to Shape Flesh for 24 hours. Each time the totenmaske Shapes Flesh, they choose one feature: ears (target becomes [[Deafened]]), eyes (target becomes [[Blinded]]), mouth (target can't speak or eat), or nose (target can't smell). A creature with both its nose and mouth sealed can't breathe and begins to suffocate. Changes are permanent until reversed by removing this curse, but the sealed flesh can be surgically opened with a successful DC 25 [[Medicine]] check that takes 1d4 rounds and deals 1d6 slashing damage per round."
armorclass:
  - name: AC
    desc: "24; **Fort** +15, **Ref** +17, **Will** +13"
health:
  - name: HP
    desc: "130; void healing; **Immunities** bleed, death effects, disease, paralyzed, poison"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +18 (`pf2:1`) (finesse, magical), **Damage** 2d6+7 piercing plus 2d6 void"
  - name: "Melee strike"
    desc: "Claw +18 (`pf2:1`) (agile, finesse, magical), **Damage** 2d8+7 slashing"
spellcasting: []
abilities_bot:
  - name: "Drink Flesh"
    desc: "`pf2:1` **Requirements** The totenmaske hit the same creature with two claw Strikes this turn and is still adjacent to it <br>  <br> **Effect** The totenmaske drains flesh from the creature's body. The creature becomes [[Sickened]] 2 and [[Drained]] 1 unless it succeeds at a DC 25 [[Fortitude]] save (sickened 2 and [[Drained]] 2 on a critical failure)."
  - name: "Living Form"
    desc: "`pf2:1` The totenmaske takes the appearance of a Medium or smaller humanoid creature. This is either their form from before they became undead or the form of the last creature they successfully drained with Drink Flesh. <br>  <br> This doesn't change the totenmaske's Speed or the attack and damage bonuses for their Strikes but might change the damage type their Strikes deal (typically to bludgeoning)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Spawned by the same unnatural and self-destructive obsessions that drove them when they still lived, totenmaskes are the undead remnants of the most self-indulgent and sinful among mortals. Their need for indulgence proved stronger than even the grasp of death, raising them from their graves. Though unable to sate their depraved desires, these foul undead can drain the very flesh from their victims so as to wrap themselves in a perverse mockery of life that allows them to pursue their base wants. Totenmaskes' specific longings vary—one might be obsessed with food or drink, while another might be vain and desirous of an attractive form to marvel at in a mirror, while yet another could simply long for the scent of blood.

Whatever sensation the totenmaske seeks, it's always a vice taken to the extreme, for this sin helped condemn them to undeath in the first place. A totenmaske obsessed with food, for example, might find themself assaulting bakeries or breweries, while a vain totenmaske obsessed with glamor could quickly grow bored of each new look and switch their victims out daily, or even hourly.

```statblock
creature: "Totenmaske"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
