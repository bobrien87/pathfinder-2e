---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "God Caller"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19"
languages: "Common, Fey (telepathy 100 feet (with eidolon only))"
skills:
  - name: Skills
    desc: "Athletics +20, Intimidation +21, Nature +19, Religion +15, Survival +15"
abilityMods: ["+4", "+2", "+1", "+0", "+3", "+5"]
abilities_top:
  - name: "Bonded Eidolon"
    desc: "The god caller fights alongside a mystical ally called an eidolon, most likely the [[Beast Eidolon]]. The eidolon has the standard number of actions, uses its normal stat block, and counts toward the encounter's XP budget normally. The eidolon must remain within 100 feet of the god caller, or its physical form will dissolve. The god caller can make their eidolon take form or disappear with the Manifest Eidolon action."
  - name: "Tandem Trick"
    desc: "**Frequency** once per round <br>  <br> **Effect** The god caller uses a team tactic with their eidolon, chosen from the following list, with the listed number of actions and traits. <br>  <br> - **Enlarge** `pf2:2` (concentrate, manipulate) The god caller casts [[Enlarge]] on their eidolon even if the eidolon is beyond range or line of effect. The god caller doesn't need to expend a spell slot, and can choose 2nd or 4th rank. <br> - **Tandem Strike** `pf2:2` The god caller makes a Strike and their eidolon can Strike as a reaction. Both attacks count toward the god caller's multiple attack penalty, but the penalty doesn't increase until both attacks have been made. <br> - **Transfer** `pf2:1` The god caller transfers 50 HP from themself to their eidolon or vice versa. If the creature losing HP has 50 HP or fewer, this effect transfers as many HP as possible without reducing that creature below 1 HP. <br> - **Transpose** `pf2:1` (concentrate, manipulate, teleportation) The god caller and their eidolon teleport to swap places."
armorclass:
  - name: AC
    desc: "29; **Fort** +18, **Ref** +16, **Will** +19"
health:
  - name: HP
    desc: "150"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +20 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning"
  - name: "Melee strike"
    desc: "War Flail +21 (`pf2:1`) (disarm, magical, sweep, trip), **Damage** 2d10+10 bludgeoning"
spellcasting:
  - name: "Primal Spontaneous Spells"
    desc: "DC 29, attack +21<br>**5th** (2 slots) [[Howling Blizzard]], [[Impaling Spike]]<br>**4th** (2 slots) [[Wall of Fire]], [[Weapon Storm]]<br>**1st** [[Electric Arc]], [[Gouging Claw]], [[Guidance]], [[Light]], [[Tangle Vine]]"
abilities_bot:
  - name: "Beseech the Spirits"
    desc: "`pf2:1` **Frequency** once per day <br>  <br> **Effect** The god caller reaches out to local entities for enhanced perception and perspective. The god caller gains lifesense 60 feet and all-around vision for 10 minutes. The god caller can't use this ability again until after propitiating the spirits during their next daily preparation."
  - name: "Manifest Eidolon"
    desc: "`pf2:3` The god caller causes their eidolon to manifest in a space adjacent to them if it's unmanifested, or to unmanifest and disappear from physical reality if it was already manifested."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The summoners called god callers have a magical link to eidolons, revered as gods by the people of Sarkoris. Though this NPC is based on Sarkorian god callers, they can be adapted to different types of summoners by changing out the eidolon for another creature and making thematic tweaks to skills and spells.

Hidden secrets and occult powers have an irresistible lure for many. Since the majority of these NPCs are spellcasters, consider using alternative spell lists to adjust their themes.

God Callers and the DivineSome spirits called by god callers of Sarkoris are divine beings capable of granting spells. Consider granting a god caller NPC a cleric focus spell appropriate to one of the god's domains if they worship such a deity (using the same DC and spell attack as their primal spells). For instance, the Stag Mother of the Forest of Stones might grant the savor the sting domain spell from the pain domain.

```statblock
creature: "God Caller"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
