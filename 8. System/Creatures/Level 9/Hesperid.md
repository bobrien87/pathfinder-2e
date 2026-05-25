---
type: creature
group: ["Fey", "Light"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hesperid"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fey"
trait_02: "Light"
trait_03: "Nymph"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19; [[Low-Light Vision]]"
languages: "Common, Fey, Utopian"
skills:
  - name: Skills
    desc: "Acrobatics +19, Athletics +11, Deception +19, Diplomacy +21, Intimidation +19, Nature +19, Performance +21, Society +17, Stealth +17"
abilityMods: ["+0", "+6", "+4", "+4", "+4", "+6"]
abilities_top: []
armorclass:
  - name: AC
    desc: "27; **Fort** +15, **Ref** +21, **Will** +19"
health:
  - name: HP
    desc: "175; **Weaknesses** cold iron 10"
abilities_mid:
  - name: "Sunset Dependent"
    desc: "A hesperid is mystically bonded to a single remote location with a good view of the sunset-usually an island, coastal cliff, or valley. If they aren't at that location and able to see the sky at sunset on any given day, they become [[Drained]] 1, increasing the value by 1 for each missed sunset and reducing by 1 only when they see the sunset. <br>  <br> A hesperid can perform a 24-hour ritual to bond to a new location."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sunset Ribbon +21 (`pf2:1`) (agile, finesse), **Damage** 2d10+6 slashing plus 1d6 fire plus 1d6 vitality"
  - name: "Ranged strike"
    desc: "Sunset Ray +21 (`pf2:1`) (magical, range 60 ft.), **Damage** 2d12+6 fire plus 1d6 vitality"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 28, attack +20<br>**3rd** [[Holy Light]]<br>**2nd** [[Revealing Light]]<br>**1st** [[Heal]], [[Illusory Disguise]], [[Light]]"
abilities_bot:
  - name: "Create Golden Apple"
    desc: "`pf2:2` While the hesperid is within their bonded location, they can spin golden light around an object they're holding of up to 20 cubic feet in volume and up to 80 Bulk. Doing so condenses the object into a magic apple made of golden light with light Bulk. <br>  <br> The golden apple reverts back to its original shape after a full day away from the hesperid's bonded location, or when the hesperid spends a single action (which has the concentrate trait) to end the effect."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Hesperides are nymphs of sunset, guardians of the colorful golden hues of the setting sun. They live on remote islands, isolated coastal cliffsides, and hidden valleys, all places where the sunset's golden glow can have the strongest effect. Hesperides manipulate sunlight with dancelike motions, allowing them to create graceful ribbons of light at close range and searing rays at a distance. Due to their connection to the beauty of the daily cycle of the setting sun, hesperides take a deep satisfaction from methodical routine that can feel alien to wilder, more chaotic fey.

Nymphs are fey guardians of nature possessed of great beauty and forms that meld breathtaking humanoid features with the natural elements they guard. Nymph queens are powerful nymphs who rule over and protect a much greater territory of untouched wilderness. For instance, a lampad might guard a beautiful underground cavern, but a lampad queen might call an entire system of caves their domain.

```statblock
creature: "Hesperid"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
