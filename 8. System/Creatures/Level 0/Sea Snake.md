---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sea Snake"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +2, Stealth +5, Survival +5"
abilityMods: ["+0", "+3", "+1", "-4", "+1", "-2"]
abilities_top:
  - name: "Deep Breath"
    desc: "The sea snake can hold its breath for about an hour."
  - name: "Sea Snake Venom"
    desc: "**Saving Throw** DC 16 [[Fortitude]] save <br>  <br> **Maximum Duration** 4 rounds <br>  <br> **Stage 1** 1d6 poison damage (1 round) <br>  <br> **Stage 2** 1d6 poison damage and [[Enfeebled]] 1 (1 round)"
armorclass:
  - name: AC
    desc: "16; **Fort** +5, **Ref** +9, **Will** +3"
health:
  - name: HP
    desc: "15"
abilities_mid:
  - name: "Lash Out"
    desc: "`pf2:r` **Trigger** A creature within the sea snake's reach uses a move action <br>  <br> **Effect** The sea snake makes a fangs Strike against the attacker."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +7 (`pf2:1`) (agile, finesse), **Damage** 1d8 piercing plus [[Sea Snake Venom]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These lithe snakes like to frequent the shallow waters of tropical seas. Their 4-foot-long, blue-green bodies easily blend into the water where they lurk to ambush prey. Sea snakes are highly venomous but often choose not to inject their venom when biting, so encounters with them rarely result in fatalities.

Tales speak of massive sea snakes that swim in deeper waters and stalk ships, waiting for sailors to fall overboard or even climbing over the side to snatch them from the deck.

Snakes of some variety thrive in every non-arctic ecosystem, each with their own particular hunting patterns and defense mechanisms.

```statblock
creature: "Sea Snake"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
